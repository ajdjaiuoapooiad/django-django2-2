


from django import forms

from core.models import Post


class CreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields= ['user','text']