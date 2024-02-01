from django.shortcuts import render
from django.middleware.csrf import get_token
# Create your views here.

def index(request):
    template_name = 'index.html'
    csrf_token = get_token(request)
    context = {'csrf_token': csrf_token}
    return render(request, template_name, context)
    