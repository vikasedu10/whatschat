from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from chat.models import Room, Message

def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    params = {
        'username': username,
        'room': room,
        'room_details': room_details,
    }
    return render(request, 'room.html', params)

def check_room(request):
    if request.method == 'POST':
        room = request.POST['room_name']
        username = request.POST['username']

        if Room.objects.filter(name=room).exists():
            return redirect(f'/'+room+'/?username='+username)
        else:
            new_room = Room.objects.create(name=room)
            new_room.save()
            return redirect(f'/'+room+'/?username='+username)
    else:
        return HttpResponse("Get request")

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse("Message Saved")

def get_messages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})