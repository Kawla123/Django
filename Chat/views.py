from django.shortcuts import render


def index(request):
    """Page d'accueil du chat"""
    return render(request, 'chat/index.html')


def room(request, room_name):
    """Page de chat pour une room spécifique"""
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

