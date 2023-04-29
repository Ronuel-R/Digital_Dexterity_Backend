"""
ASGI config for Digital_Dex_Backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
### Websocket ###
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import digital_dex_admin_web.versions.v1p0.features.landing_page.routing.routing
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            digital_dex_admin_web.versions.v1p0.features.landing_page.routing.routing.websocket_urlpatterns
        )
    )
})
