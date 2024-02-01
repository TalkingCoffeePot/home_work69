from django.shortcuts import render
from django.views.generic import View
import json
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
# Create your views here.

def sign_choice(path, a, b):
    answer = 0
    if 'add' in path:
        answer = a+b
    elif 'subtract' in path:
        answer = a-b
    elif 'multiply' in path:
        answer = a*b
    elif 'divide' in path:
        if a!=0 or b!=0:
            answer = a/b
        else:
            answer = 'Divided by Zero'
    return answer

class MathView(View):
    def post(self, request, *args, **kwargs):
        answer = {}
        print(request.body)
        if request.body:
            data = json.loads(request.body)
            
            try:
                answer['answer'] = sign_choice(request.path, data['A'], data['B'])
            except:
                answer['error'] = 'Wrong Data Type'
        else:
            answer['error'] = 'No Data'
        return JsonResponse(answer)
