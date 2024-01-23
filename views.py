from django.shortcuts import render
from .models import QA

def chatbot(request):
    all_qa = QA.objects.all()
    return render(request, 'chatbot/chatbot.html', {'all_qa': all_qa})
