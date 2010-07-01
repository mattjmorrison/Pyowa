from django import forms
from Pyowa.microblog import models

class MicroblogForm(forms.ModelForm):

    class Meta:
        model = models.Microblog