import json

from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.
def deposit(request):
    data = json.loads(request.body, encoding='utf-8')
    filename = data['filename']
    return JsonResponse({'status': 'OK'})

def retreive(request):
    data = json.loads(request.body, encoding='utf-8')
    filename = data['filename']
    return JsonResponse({'status': 'OK'})