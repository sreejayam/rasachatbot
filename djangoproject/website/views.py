


# # import requests
# # from django.shortcuts import render,redirect
# #
# # from .models import ChatMessage
# # from .forms import ChatForm
# #
# # RASA_API_ENDPOINT = 'http://localhost:5005/webhooks/rest/webhook'  # Replace with your Rasa API endpoint
# # def clear_messages():
# #     ChatMessage.objects.all().delete()
# #
# # # Clear messages when the Django server starts
# # clear_messages()
# # def get_rasa_response(message, conversation_history):
# #     data = {
# #         "sender": "user",
# #         "message": message,
# #         "metadata": {"conversation_history": conversation_history}
# #     }
# #     try:
# #         response = requests.post(RASA_API_ENDPOINT, json=data)
# #         response.raise_for_status()
# #         return response.json()
# #     except requests.RequestException as e:
# #         return [{'text': f"Error communicating with Rasa server: {e}"}]
# #
# # def chat_view(request):
# #     if request.method == 'POST':
# #         form = ChatForm(request.POST)
# #         if form.is_valid():
# #             user_message = form.cleaned_data['message']
# #
# #             # Retrieve conversation history from previous messages
# #             conversation_history = list(ChatMessage.objects.values_list('content', flat=True))
# #
# #             ChatMessage.objects.create(content=f'User: {user_message}')
# #
# #             # Get Rasa response with conversation history
# #             rasa_response = get_rasa_response(user_message, conversation_history)
# #             bot_response = rasa_response[0]['text'] if rasa_response else 'Sorry, I didn\'t understand that.'
# #
# #             ChatMessage.objects.create(content=f'Bot: {bot_response}')
# #
# #             return redirect('chat_view')
# #     else:
# #         form = ChatForm()
# #
# #     messages = ChatMessage.objects.all()
# #
# #     return render(request, 'chat.html', {'form': form, 'messages': messages})
# # views.py
# import requests
# from django.shortcuts import render, redirect
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import ChatMessage
# from .forms import ChatForm
# from .serializer import ChatMessageSerializer
#
# RASA_API_ENDPOINT = 'http://localhost:5005/webhooks/rest/webhook'  # Replace with your Rasa API endpoint
#
# def clear_messages():
#     ChatMessage.objects.all().delete()
#
# # Clear messages when the Django server starts
# clear_messages()
#
# def get_rasa_response(message, conversation_history):
#     data = {
#         "sender": "user",
#         "message": message,
#         "metadata": {"conversation_history": conversation_history}
#     }
#     try:
#         response = requests.post(RASA_API_ENDPOINT, json=data)
#         response.raise_for_status()
#         return response.json()
#     except requests.RequestException as e:
#         return [{'text': f"Error communicating with Rasa server: {e}"}]
#
# class ChatAPIView(APIView):
#     def get(self, request):
#         messages = ChatMessage.objects.all()
#         serializer = ChatMessageSerializer(messages, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         form = ChatForm(request.data)
#         if form.is_valid():
#             user_message = form.cleaned_data['message']
#
#             # Retrieve conversation history from previous messages
#             conversation_history = list(ChatMessage.objects.values_list('content', flat=True))
#
#             ChatMessage.objects.create(content=f'User: {user_message}')
#
#             # Get Rasa response with conversation history
#             rasa_response = get_rasa_response(user_message, conversation_history)
#             bot_response = rasa_response[0]['text'] if rasa_response else 'Sorry, I didn\'t understand that.'
#
#             ChatMessage.objects.create(content=f'Bot: {bot_response}')
#
#             return Response({"message": "Chat message processed successfully"}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"error": "Invalid form data"}, status=status.HTTP_400_BAD_REQUEST)
#
# def chat_view(request):
#     if request.method == 'POST':
#         form = ChatForm(request.POST)
#         if form.is_valid():
#             user_message = form.cleaned_data['message']
#
#             # Retrieve conversation history from previous messages
#             conversation_history = list(ChatMessage.objects.values_list('content', flat=True))
#
#             ChatMessage.objects.create(content=f'User: {user_message}')
#
#             # Get Rasa response with conversation history
#             rasa_response = get_rasa_response(user_message, conversation_history)
#             bot_response = rasa_response[0]['text'] if rasa_response else 'Sorry, I didn\'t understand that.'
#
#             ChatMessage.objects.create(content=f'Bot: {bot_response}')
#
#             return redirect('chat_view')
#     else:
#         form = ChatForm()
#
#     messages = ChatMessage.objects.all()
#
#     return render(request, 'chat.html', {'form': form, 'messages': messages})
# import requests
# from django.shortcuts import render,redirect
#
# from .models import ChatMessage
# from .forms import ChatForm
#
# RASA_API_ENDPOINT = 'http://localhost:5005/webhooks/rest/webhook'  # Replace with your Rasa API endpoint
# def clear_messages():
#     ChatMessage.objects.all().delete()
#
# # Clear messages when the Django server starts
# clear_messages()
# def get_rasa_response(message, conversation_history):
#     data = {
#         "sender": "user",
#         "message": message,
#         "metadata": {"conversation_history": conversation_history}
#     }
#     try:
#         response = requests.post(RASA_API_ENDPOINT, json=data)
#         response.raise_for_status()
#         return response.json()
#     except requests.RequestException as e:
#         return [{'text': f"Error communicating with Rasa server: {e}"}]
#
# def chat_view(request):
#     if request.method == 'POST':
#         form = ChatForm(request.POST)
#         if form.is_valid():
#             user_message = form.cleaned_data['message']
#
#             # Retrieve conversation history from previous messages
#             conversation_history = list(ChatMessage.objects.values_list('content', flat=True))
#
#             ChatMessage.objects.create(content=f'User: {user_message}')
#
#             # Get Rasa response with conversation history
#             rasa_response = get_rasa_response(user_message, conversation_history)
#             bot_response = rasa_response[0]['text'] if rasa_response else 'Sorry, I didn\'t understand that.'
#
#             ChatMessage.objects.create(content=f'Bot: {bot_response}')
#
#             return redirect('chat_view')
#     else:
#         form = ChatForm()
#
#     messages = ChatMessage.objects.all()
#
#     return render(request, 'chat.html', {'form': form, 'messages': messages})
import requests
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ChatMessage
from .forms import ChatForm
from knox.models import AuthToken

from knox.models import AuthToken  # Import AuthToken from knox
from .serializer import ChatMessageSerializer
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication  # Import TokenAuthentication from knox

RASA_API_ENDPOINT = 'http://localhost:5005/webhooks/rest/webhook'  # Replace with your Rasa API endpoint

def clear_messages():
    ChatMessage.objects.all().delete()

# Clear messages when the Django server starts
clear_messages()

def get_rasa_response(message, conversation_history):
    data = {
        "sender": "user",
        "message": message,
        "metadata": {"conversation_history": conversation_history}
    }
    try:
        response = requests.post(RASA_API_ENDPOINT, json=data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return [{'text': f"Error communicating with Rasa server: {e}"}]

class ChatAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Only authenticated users can reach this point
        user = request.user
        messages = ChatMessage.objects.filter(user=user)
        serializer = ChatMessageSerializer(messages, many=True)
        return Response(serializer.data)

    # ... (previous code)
    # ... (previous code)
    def post(self, request):
        form = ChatForm(request.data)
        if form.is_valid():
            user_message = form.cleaned_data['message']

            # Retrieve conversation history from previous messages
            conversation_history = list(ChatMessage.objects.values_list('content', flat=True))

            ChatMessage.objects.create(content=f'User: {user_message}', user=request.user)

            # Get Rasa response with conversation history
            rasa_response = get_rasa_response(user_message, conversation_history)
            bot_response = rasa_response[0]['text'] if rasa_response else 'Sorry, I didn\'t understand that.'

            # Create an AuthToken for the user
            auth_token, _ = AuthToken.objects.create(request.user)

            ChatMessage.objects.create(content=f'Bot: {bot_response}', user=request.user)

            # Convert AuthToken to a string before including it in the response
            auth_token_str = str(auth_token)

            return Response({"message": "Chat message processed successfully", "token": auth_token_str},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Invalid form data"}, status=status.HTTP_400_BAD_REQUEST)


# The rest of your views remain unchanged
# def chat_view(request):
#     if request.method == 'POST':
#         form = ChatForm(request.POST)
#         if form.is_valid():
#             user_message = form.cleaned_data['message']
#
#             # Retrieve conversation history from previous messages
#             conversation_history = list(ChatMessage.objects.values_list('content', flat=True))
#
#             ChatMessage.objects.create(content=f'User: {user_message}')
#
#             # Get Rasa response with conversation history
#             rasa_response = get_rasa_response(user_message, conversation_history)
#             bot_response = rasa_response[0]['text'] if rasa_response else 'Sorry, I didn\'t understand that.'
#
#             ChatMessage.objects.create(content=f'Bot: {bot_response}')
#
#             return redirect('chat_view')
#     else:
#         form = ChatForm()
#
#     messages = ChatMessage.objects.all()
#
#     return render(request, 'chat.html', {'form': form, 'messages': messages})
from django.contrib.auth import get_user_model

def chat_view(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['message']

            # Retrieve conversation history from previous messages
            conversation_history = list(ChatMessage.objects.values_list('content', flat=True))

            # Get the currently logged-in user
            User = get_user_model()
            user = request.user

            # Ensure that the user is a CustomUser instance
            if isinstance(user, User):
                # Create a ChatMessage object with the user
                ChatMessage.objects.create(content=f'User: {user_message}', user=user,show_buttons=True)

                # Get Rasa response with conversation history
                rasa_response = get_rasa_response(user_message, conversation_history)
                bot_response = rasa_response[0]['text'] if rasa_response else 'Sorry, I didn\'t understand that.'

                # Create ChatMessage objects for the bot response
                ChatMessage.objects.create(content=f'Bot: {bot_response}', user=user)

                return redirect('chat_view')

    else:
        form = ChatForm()

    messages = ChatMessage.objects.all()

    return render(request, 'chat.html', {'form': form, 'messages': messages})