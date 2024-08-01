# # Topic - Routing
# from channels.consumer import SyncConsumer,AsyncConsumer
# from channels.exceptions import StopConsumer

# class MySyncConsumer(SyncConsumer):
#      def websocket_connect(self,event):
#           print("websocket connected",event)
#           # for two connection
#           self.send({
#                'type':'websocket.accept'
#           })

#      #    frontened to backened 
#      # when client msg send 
#      def websocket_receive(self,event):
#           print("websocket receive",event)
#           print("message is ",event['text'])
          
#      def websocket_disconnect(self,event):
#           print("websocket disconnected",event)
#           raise StopConsumer()

# class MyAsyncConsumer(AsyncConsumer):
#      async def websocket_connect(self,event):
#           print("websocket connected",event)
#           await self.send({
#                'type':'websocket.accept'
#           })
         
          
#      async def websocket_receive(self,event):
#           print("websocket reseive",event)
#           print("message is ",event['text'])

#      async def websocket_disconnect(self,event):
#           print("websocket disconnected",event)

# more on consumer and routing
from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer

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
          self.send({
               'type':'websocket.send',
               'text':'msg sent to client from application'
          })
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
          await self.send({
               'type':'websocket.send',
               'text':'msg sent to client from application'
          })
     async def websocket_disconnect(self,event):
          print('websocket disconnected....',event)     
          raise StopConsumer()