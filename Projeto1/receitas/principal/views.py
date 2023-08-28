from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Novo texto!')

def sobre(request):
    return HttpResponse('Funcionou')

def contato(request):
    return HttpResponse('(14) 11111-1111')