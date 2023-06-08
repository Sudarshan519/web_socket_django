"""
ASGI config for myproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path

import myapp.routing 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# application = ProtocolTypeRouter(
#     {
#         "http": get_asgi_application(),
#         # Just HTTP for now. (We can add other protocols later.)
#     }
# )
application = ProtocolTypeRouter({"http":get_asgi_application(),
                                  "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter( 
                 myapp.routing.websocket_urlpatterns
                # path("chat/", PublicChatConsumer.as_asgi()),
           )
        )
    ),
})
# get_asgi_application()
