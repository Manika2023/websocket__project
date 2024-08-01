
# import os

# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter,URLRouter
# import app.routing

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs8.settings')

# application = ({
#      'http':get_asgi_application(),
#      'websocket':URLRouter(
#           app.routing.websocket_urlpatterns
#      )
# })


import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from app import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs8.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})

