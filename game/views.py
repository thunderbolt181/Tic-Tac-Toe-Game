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
        print(request.data)
        p_game=request.data
        game=TicTakToe.board()
        board = game.computer_game(p_game,False)
        print(board)
        return Response({"request":board})
        # for i in range(3):
        #     for j in range(3):
        #         print(p_game[i][j],board[i][j])
        #         if p_game[i][j] != board[i][j]:
        #             return Response({"request":f"{i}{j}"})
        # else:
        #     return Response({"request":"No turn"})