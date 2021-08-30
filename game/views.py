from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import TicTakToe

def load_game(request):
    return render(request,'game.html')

class play_game(viewsets.ViewSet):
    permission_classes=(AllowAny,)

    def list(self,request,*args,**kwargs):
        print("hello")
        return Response({"Hello":'hello'})

    def create(self,request,*args,**kwargs):
        game=TicTakToe.board()
        win=game.check_win(request.data)
        if win:
            return Response({"request":request.data,"win":True})
        board = game.computer_game(request.data,False)
        win=game.check_win(request.data)
        if win:
            return Response({"request":board,"win":False})
        else:
            return Response({"request":board,"win":None})