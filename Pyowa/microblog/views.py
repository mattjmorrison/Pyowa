from django import http
from django.core.urlresolvers import reverse
from Pyowa.microblog import models, forms
from Pyowa.shortcuts import views

@views.render_to('index.html')
def index(request):
    return {'blogs':models.Microblog.objects.select_related().all()}

@views.render_to('edit.html')
def edit(request, id):
    blog = models.Microblog.objects.get(id=id)
    if request.method == "POST":
        form = forms.MicroblogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return http.HttpResponseRedirect(reverse('microblog:index'))
        else:
            return {'form': form, 'blog':blog}
    else:
        return {'form': forms.MicroblogForm(instance=blog), 'blog':blog}
