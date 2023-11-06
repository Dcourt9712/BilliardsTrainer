from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['author', 'content']

class CreateNewUser(forms.Form):
    username = forms.CharField(label="Username",max_length=200)
    email = forms.CharField(label="Email",max_length=200)
    password = forms.CharField(label="Password",max_length=20)

