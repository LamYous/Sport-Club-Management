from django import forms
from .models import Member, Coach
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'palceholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = '__all__'