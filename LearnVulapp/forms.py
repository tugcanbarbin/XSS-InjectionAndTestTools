from django import forms
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import Textarea
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('nickname','body')
         
        widgets={
            'nickname' : forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
        }
class Commentf(forms.Form):
    nickname = forms.CharField(label='NickName',max_length=100)
    body = forms.TimeField(label="Comment Here")
