from django.shortcuts import render, redirect

from .forms import MessageForm
from .models import ChatRoom, Message


def chat_room(request, room_id):
    room = ChatRoom.objects.get(id=room_id)
    messages = Message.objects.filter(room=room).order_by('timestamp')
    form = MessageForm()
    return render(request, 'chat/chat_room.html', {'room': room, 'messages': messages, 'form': form})


def create_message(request, room_id):
    room = ChatRoom.objects.get(id=room_id)
    form = MessageForm(request.POST)
    if form.is_valid():
        content = form.cleaned_data['content']
        message = Message.objects.create(room=room, content=content)
    return redirect('chat:chat_room', room_id=room.id)


def index(request):
    return render(request, 'chat/chat_index.html', {})


def room(request, room_name):
    return render(request, 'chat/chatroom.html', {
        'room_name': room_name
    })
