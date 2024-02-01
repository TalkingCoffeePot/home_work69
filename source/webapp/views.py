from django.shortcuts import render
from django.middleware.csrf import get_token
# Create your views here.

def index(request):
    template_name = 'index.html'
    return render(request, template_name)
    