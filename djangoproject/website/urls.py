
from django.urls import path
from .views import *

urlpatterns = [
    path('api/', ChatAPIView.as_view(), name='chat-api'),

    path('chat/', chat_view, name='chat_view'),
]
