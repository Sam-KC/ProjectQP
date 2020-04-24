from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
import datetime

@csrf_exempt
def index(request):

    if request.method == 'POST':
        return postrequest()
    else:
        return postrequest()


def postrequest():
    response = {
    'name': 'Vitor',
    'location': 'Finland',
    'is_active': True,
    'count': 28
    }
    return JsonResponse(response)


def httprequest():
    now = datetime.datetime.now()
    response = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(response)

