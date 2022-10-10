from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        self.__init__(request, *args, **kwargs)

        self.fields['username'].label = 'Name'
        self.error_messages['invalid_login'] = 'INVALID CREDENTIALS!!! Name and password maybe case-senstitive.'


class SignupForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Voters
        fields = '__all__'
        exclude = ['id']