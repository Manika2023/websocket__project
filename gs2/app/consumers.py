# Topic- Consumer

from channels.consumer import SyncConsumer,AsyncConsumer

class MySyncConsumer(SyncConsumer):
     # this handler is called when client initially opens a 
     # connection and is about to finish the websocket handshake
     def websocket_connect(self,event):
          print("web socket connected.....")

     # this handler is called when data is received from client
     def websocket_receive(self,event):
          print("Message Received")     

     # tthis handler is called when either connection to the client is lost
     # either from the client closing the connection , the server closing the connection 
     # or loss of the socket
     def websocket_discoonect(self,event):
          print("websocket disconnected....")     


class MySyncConsumer(AsyncConsumer):
     # this handler is called when client initially opens a 
     # connection and is about to finish the websocket handshake
     async def websocket_connect(self,event):
          print("web socket connected.....")

     # this handler is called when data is received from client
     async def websocket_receive(self,event):
          print("Message Received")     

     # tthis handler is called when either connection to the client is lost
     # either from the client closing the connection , the server closing the connection 
     # or loss of the socket
     async def websocket_discoonect(self,event):
          print("websocket disconnected....")     