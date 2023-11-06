from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['author', 'content']

class CreateNewUser(forms.Form):
    username = forms.CharField(label="Username",max_length=200)
    email = forms.CharField(label="Email",max_length=200)
<<<<<<< HEAD
    password = forms.CharField(label="Password",max_length=20, widget=forms.PasswordInput())


class loginForm(forms.Form):
    #username = forms.CharField(label="Username",max_length=200)
    #password = forms.CharField(label="Password",max_length=20, widget=forms.PasswordInput())
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
=======
    password = forms.CharField(label="Password",max_length=20)

>>>>>>> 79646b893e15b89938c1df3b40c98ded2016a0fa
