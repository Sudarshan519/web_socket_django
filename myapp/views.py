from django.shortcuts import render

# Create your views here.
def lobby(request):
    return render(request,'myapp/lobby.html')


def room(request, room_name):
    return render(request, "myapp/room.html", {"room_name": room_name})