from django import forms
from .models import Message
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']

    def save(self, commit=True, user=None):
        instance = super(MessageForm, self).save(commit=False)
        if user:
            instance.author = user
        if commit:
            instance.save()
        return instance

class CreateNewUser(forms.ModelForm):
    username = forms.CharField(label="Username",max_length=200)
    email = forms.CharField(label="Email",max_length=200)
    password = forms.CharField(label="Password",max_length=20, widget=forms.PasswordInput())

    class Meta:
            model = User
            fields = ('username', 'email', 'password')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered")
        return email

class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
