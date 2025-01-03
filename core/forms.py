


from django import forms

from core.models import Comment, Post


class CreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields= ['user','text']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields= ['text']