from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

def load_game(request):
    return render(request,'game.html')

class play_game(viewsets.ViewSet):
    permission_classes=(AllowAny,)

    def list(self,request,*args,**kwargs):
        print("hello")
        return JsonResponse({"Hello":'hello'})