from django.urls import path

from .views import ChatGPTAPIView


urlpatterns = [
    path('chat-gpt/', ChatGPTAPIView.as_view(), name='chat-gpt'),
]
