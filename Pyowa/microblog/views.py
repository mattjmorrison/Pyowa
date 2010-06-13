# Create your views here.
#from django.http import HttpResponse

from django import shortcuts


def index(request):
    return shortcuts.render_to_response("index.html")
    #return HttpResponse("There!!!")