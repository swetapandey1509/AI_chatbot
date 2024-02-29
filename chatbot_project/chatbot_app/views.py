from django.shortcuts import render
from django.http import JsonResponse
from nltk.chat.util import Chat, reflections
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt  # Add this import

pattern_response_pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am just a chatbot, but I am here to help. How can I assist you?']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Have a great day!']),
]

chatbot = Chat(pattern_response_pairs, reflections)

@csrf_exempt  # Add this decorator to handle POST without CSRF token (for simplicity, in production, use CSRF tokens)
def chatbot_view(request):
    template = get_template('chatbot_app/chatbot.html')
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        response = chatbot.respond(user_input)
        return JsonResponse({'response': response})
    return render(request, 'chatbot_app/chatbot.html', {'response': ''})
