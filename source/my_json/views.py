from django.shortcuts import render
from django.views.generic import View
import json
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def sign_choice(path, a, b):
    a, b = int(a), int(b)
    answer = 0
    
    if 'add' in path:
        answer = a+b
    elif 'substract' in path:
        answer = a-b
    elif 'multiply' in path:
        answer = a*b
    elif 'divide' in path:
        if a!=0 or b!=0:
            answer = a/b
        else:
            answer = 'Divided by Zero'
    return answer


@method_decorator(csrf_exempt, name='dispatch')
class MathView(View):
    def post(self, request, *args, **kwargs):
        answer = {}
        if request.body:
            data = json.loads(request.body)
            
            try:
                answer['answer'] = sign_choice(request.path, data['A'], data['B'])
            except:
                answer['error'] = 'Wrong Data Type'
        else:
            answer['error'] = 'No Data'
        return JsonResponse(answer)
