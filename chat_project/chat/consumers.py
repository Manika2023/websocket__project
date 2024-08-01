# chat/consumers.py
import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.core.exceptions import MultipleObjectsReturned
from .models import ChatMessage, Room_Name

# chat/consumers.py
import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.utils import timezone
from .models import ChatMessage, Room_Name

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept the WebSocket connection
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_disconnect(self, event):
        # Called when the WebSocket closes for any reason
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def websocket_receive(self, event):
        # Called when a message is received from the WebSocket
        data = json.loads(event['text'])
        # actual msg without key
        message = data.get('message')

        # Save the message and room name to the database
        timestamp = timezone.now().strftime('%H:%M:%S')  # Format timestamp as HH:MM:SS
        try:
            await self.save_message(self.room_name, message, timestamp)
        except MultipleObjectsReturned:
            print(f"Multiple rooms found for {self.room_name}, this should be fixed.")

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'timestamp': timestamp
            }
        )

    async def chat_message(self, event):
        # Receive message from room group
        message = event['message']
        timestamp = event['timestamp']

        # Send message to WebSocket
        await self.send({
            'type': 'websocket.send',
            'text': json.dumps({
                'message': message,
                'timestamp': timestamp
            })
        })

    @database_sync_to_async
    def save_message(self, room_name, message, timestamp):
        try:
            room = Room_Name.objects.filter(room_name=room_name).first()
        except Room_Name.DoesNotExist:
            room = Room_Name.objects.create(room_name=room_name)
        except MultipleObjectsReturned:
            room = Room_Name.objects.filter(room_name=room_name).first()
        # Save the message to the database with timestamp
        ChatMessage.objects.create(content=message, group=room, timeStamp=timezone.now())
