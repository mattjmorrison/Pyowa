from django import shortcuts
from Pyowa.microblog import models

def index(request):
    return shortcuts.render_to_response("index.html", {'blogs':models.Microblog.objects.all()})