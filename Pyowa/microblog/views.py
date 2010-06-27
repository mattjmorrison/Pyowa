from Pyowa.microblog import models
from Pyowa.shortcuts import views


@views.render_to('index.html')
def index(request):
    return {'blogs':models.Microblog.objects.select_related().all()}