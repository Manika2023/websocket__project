# from django.urls import path
# from . import consumers

# websocket_urlpatterns = [
#      path('ws/sc/',consumers.MySyncConsumer.as_asgi()),

# ]
from django.urls import re_path,path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from app import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/sc/$', consumers.MySyncConsumer.as_asgi()),
#     re_path(r'ws/ac/$', consumers.MyAsyncConsumer.as_asgi()),
# ]
# websocket_urlpatterns = [
#     path('ws/sc/', consumers.MySyncConsumer.as_asgi()),
#     path('ws/ac/', consumers.MyAsyncConsumer.as_asgi()),
# ]

# to dynamic url
websocket_urlpatterns = [
    path('ws/sc/<str:groupkaname>/', consumers.MySyncConsumer.as_asgi()),
    path('ws/ac/', consumers.MyAsyncConsumer.as_asgi()),
]