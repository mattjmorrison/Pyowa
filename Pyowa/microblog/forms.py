from Pyowa.microblog import models
from django import forms

class MicroblogForm(forms.ModelForm):
    class Meta:
        model = models.Microblog