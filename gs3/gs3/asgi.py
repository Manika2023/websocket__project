
import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
import app.routings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs3.settings')

application = ProtocolTypeRouter({
     # keys are predefined do not use other word
     'http':get_asgi_application(),
     'websocket':URLRouter(
          app.routings.websocket_urlspatterns,
     )
})