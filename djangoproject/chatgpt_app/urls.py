from django.urls import path
from . import views
from .views import get_chatgpt_response



urlpatterns = [ path('chatgpt/', get_chatgpt_response, name='get_chatgpt_response'),

]