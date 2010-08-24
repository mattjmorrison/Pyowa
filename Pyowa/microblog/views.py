from django import http
from django.core.urlresolvers import reverse
from Pyowa.microblog import models, forms
from Pyowa.shortcuts import views

@views.render_to('microblog/templates/list.html')
def index(request):
    return {'blogs':models.Microblog.objects.select_related().all()}

@views.render_to('microblog/templates/edit.html')
def add(request):
    form = forms.MicroblogForm(request.POST or None)
    return _save_blog(form)

@views.render_to("microblog/templates/edit.html")
def edit(request, id):
    form = forms.MicroblogForm(request.POST or None, instance=models.Microblog.objects.get(pk=id))
    return _save_blog(form)

def delete(request, id):
    blog = models.Microblog.objects.get(pk=id)
    blog.delete()
    return http.HttpResponseRedirect(reverse("microblog:list"))

def _save_blog(form):
    if form.is_valid():
        form.save()
        return http.HttpResponseRedirect(reverse("microblog:list"))
    else:
        return {'form': form}
