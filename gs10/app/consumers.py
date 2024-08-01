# chat App

from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json
from .models import Group,Chat
from channels.db import database_sync_to_async

class MySyncConsumer(SyncConsumer):
     def websocket_connect(self,event):
          print("websocket connected...", event)
          # channel layer is queque
          print("channel layer")
          # get default channel layer from project
          print("channel layer...",self.channel_layer)
          # get channel name
          print("channel name...",self.channel_name)
          # "programmers=grp name and channel_name is grp member
          # to dynamic url 
          # self.group_name = variable name
          self.group_name=self.scope['url_route']['kwargs']['groupkaname']
          print("Group name.....",self.group_name)

          # add a channel to a new or existing group
          # to convert async

          # async_to_sync(self.channel_layer.group_add)("programmers",
          #                                             self.channel_name)
          async_to_sync(self.channel_layer.group_add)(
                                                      self.group_name,
                                                      self.channel_name)
          self.send({
               'type':'websocket.accept'
          })

     def websocket_receive(self,event):
          # client daTA
          print("websocket receive...", event['text'])
          print("websocket receive...", type(event['text']))
          # converting str to json object
          data = json.loads(event['text'])
          print("Chat msg: ",data['msg'])

          # to find group objects
          group = Group.objects.get(name=self.group_name)

          # creating new chat object
          chat = Chat(
               content=data['msg'],
               group=group
          )
          chat.save()
          # server to client
          async_to_sync(self.channel_layer.group_send)(self.group_name,{
               # msg in dict,msg is handler
               # chat.message=event
               'type':'chat.message',
               'message':event['text']
          })
          
          # to send client
     # chat_message= handler
     def chat_message(self,event):
          print("Event..",event)
          print("Actual data ..",event['message'])
          self.send({
               'type':'websocket.send',
               'text':event['message']
          })

          

     def websocket_disconnect(self,event):
          print("websocket disconnected...", event)
          print("channel layer...",self.channel_layer)
          # get channel name
          print("channel name...",self.channel_name)
          async_to_sync(self.channel_layer.group_discard)(self.group_name,self.channel_name)
          raise StopConsumer()
     

class MyAsyncConsumer(AsyncConsumer):
     async def websocket_connect(self,event):
          self.group_name=self.scope['url_route']['kwargs']['groupkaname']
          
          await self.channel_layer.group_add(self.group_name,
                                                      self.channel_name)
          await self.send({
               'type':'websocket.accept'
          })

     async def websocket_receive(self,event):
          data = json.loads(event['text'])
          group = await database_sync_to_async(Group.objects.get)(name=self.group_name)

          # creating new chat object
          chat = Chat(
               content=data['msg'],
               group=group
          )
          await database_sync_to_async(chat.save)()
          await self.channel_layer.group_send(self.group_name,{
               'type':'chat.message',
               'message':event['text']
          })

          # to send client
     # chat_message= handler
     async def chat_message(self,event):
          print("Event..",event)
          print("Actual data ..",event['message'])
          await self.send({
               'type':'websocket.send',
               'text':event['message']
          })

          

     async def websocket_disconnect(self,event):
          print("websocket disconnected...", event)
          print("channel layer...",self.channel_layer)
          # get channel name
          print("channel name...",self.channel_name)
          await self.channel_layer.group_discard('programmers',self.channel_name)
          raise StopConsumer()
     
