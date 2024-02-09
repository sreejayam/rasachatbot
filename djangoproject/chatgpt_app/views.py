from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
import json

@csrf_exempt
def get_chatgpt_response(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_message = data.get('user_message')

        # Use OpenAI API to get a response from ChatGPT
        openai.api_key = 'YOUR_OPENAI_API_KEY'
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=100  # Adjust as needed
        )

        chatgpt_response = response['choices'][0]['text'].strip()
        return JsonResponse({"chatgpt_response": chatgpt_response})

    # If the request method is not POST, return a simple error message
    return JsonResponse({"error": "Invalid request method. Use POST."})
