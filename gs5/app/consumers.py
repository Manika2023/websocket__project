
from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio

class MySyncConsumer(SyncConsumer):
     def websocket_connect(self,event):
          print("websocket connected...", event)
          self.send({
               'type':'websocket.accept'
          })
     def websocket_receive(self,event):
          # msg receive from client
          print("msg received from client",event)     
          # access client data
          print(event['text'])
          # application send to client
          for i in range(50):
               self.send({
               'type':'websocket.send',
               'text':str(i)
               })
               sleep(1)
               
     def websocket_disconnect(self,event):
          print('websocket disconnected....',event)     
          raise StopConsumer()
     

class MyAsyncConsumer(AsyncConsumer):
     async def websocket_connect(self,event):
          print("websocket connected...", event)
          await self.send({
               'type':'websocket.accept'
          })
     async def websocket_receive(self,event):
          # msg receive from client
          print("msg received from client",event)     
          # access client data
          print(event['text'])
          # application send to client
          for i in range(50):
               await self.send({
               'type':'websocket.send',
               'text':str(i)
               })
               await asyncio.sleep(1)
               
     def websocket_disconnect(self,event):
          print('websocket disconnected....',event)     
          raise StopConsumer()
     