from django.shortcuts import render,redirect
from .models import Room_Name
from django.shortcuts import render, get_object_or_404, redirect
from .models import Room_Name, ChatMessage
from .forms import ChatForm

def index(request):
    if request.method == 'POST':
        room_name=request.POST.get('room-name-input')
        ins = Room_Name(room_name=room_name) 
        if ins:
            room = ins.save()
            return redirect('room', room_name)
    return render(request, 'chat/index.html')

# def room(request, room_name):
#     return render(request, 'chat/room.html', {
#         'room_name': room_name
#     })

# # chat/views.py


def room(request, room_name):
    # Fetch the room object by name
    group = Room_Name.objects.filter(room_name=room_name).first()

    if not group:
        return render(request, 'chat/404.html', {'error': 'Room not found'})

    # Fetch messages related to the group
    chats = ChatMessage.objects.filter(group=group)

    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.group = group
            chat.save()
            return redirect('room', room_name=room_name)
    else:
        form = ChatForm()

    return render(request, 'chat/room.html', {'group': group, 'chats': chats, 'form': form})