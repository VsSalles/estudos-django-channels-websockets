from django.urls import re_path
from . import consumers, consumers_async

websocket_urlpatterns = [
    re_path(r'ws/app/(?P<nome>\w+)/$', consumers.TesteConsumer.as_asgi()),
]