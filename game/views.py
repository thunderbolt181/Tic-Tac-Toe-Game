from django.shortcuts import render

def load_game(request):
    return render(request,'game.html')