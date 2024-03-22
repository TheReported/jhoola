from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

def dashboard(request):
    return render(request, 'users/dashboard.html', {})

@csrf_exempt
@require_POST
def register(request):
    data = json.loads(request.body)
