from django.shortcuts import render

# Create your views here.
# chat/views.py
from django.shortcuts import render
from .models import Chat
from django.http import HttpResponse

def index(request):
    chats()
    return render(request, "chat/index.html")

def chats():
    all=Chat.objects.all()
    for chat in all:
        print(chat.message+"HI")
 