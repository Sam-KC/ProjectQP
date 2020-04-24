from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
import datetime
from django.shortcuts import render


@csrf_exempt
def index(request):
    if request.method == 'POST':
        return postrequest()
    else:
        return render(request, 'index.html')


def postrequest():   
    response = {  
    'name': 'your_name', 
    'location': 'Finland',
    'is_active': True,
    'count': 28
    }
    return JsonResponse(response)


def httprequest():
    now = datetime.datetime.now()
    response = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(response)

