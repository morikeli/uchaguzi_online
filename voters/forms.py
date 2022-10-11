from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import Voters, Aspirants


class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

        self.fields['username'].label = 'Name'
        self.error_messages['invalid_login'] = 'INVALID CREDENTIALS!!! enter correct name (first name and last name) and password. Name and password maybe case-senstitive.'


class SignupForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


class UpdateProfileForm(forms.ModelForm):
    SELECT_GENDER = (
        (None, '-- Select your gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    SELECT_SCHOOL = (
        (None, '-- Select your school --'),
    )
    SELECT_YEAR = (
        (None, '-- Select year of study --'),
        ('First Year', 'First Year (Fresher)'),
        ('Second Year', 'Second Year (Sophomore)'),
        ('Third Year', 'Third Year (Junior)'),
        ('Fourth Year', 'Fourth Year (Senior)'),
    )
    SELECT_SEMESTER = (
        (None, '-- Select semester --'),
        ('1', '1'),
        ('2', '2')
    )
    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), label='', choices=SELECT_GENDER)
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'mb-2', 'placeholder': 'Enter your mobile no.'}), label='', )
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'mb-2'}), label='', help_text='Enter your date of birth')
    school = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), label='', choices=SELECT_SCHOOL)
    year = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), label='', choices=SELECT_YEAR)
    semester = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), label='', choices=SELECT_SEMESTER)

    class Meta:
        model = Voters
        fields = '__all__'

class EditProfileForm(forms.ModelForm):
    SELECT_GENDER = (
        (None, '-- Select your gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    SELECT_SCHOOL = (
        (None, '-- Select your school --'),
    )
    SELECT_YEAR = (
        (None, '-- Select year of study --'),
        ('First Year', 'First Year (Fresher)'),
        ('Second Year', 'Second Year (Sophomore)'),
        ('Third Year', 'Third Year (Junior)'),
        ('Fourth Year', 'Fourth Year (Senior)'),
    )
    SELECT_SEMESTER = (
        (None, '-- Select semester --'),
        ('1', '1'),
        ('2', '2')
    )
    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), label='', choices=SELECT_GENDER, disabled=True)
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'mb-2', 'placeholder': 'Enter your mobile no.'}), label='', disabled=True)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'mb-2'}), label='', help_text='Enter your date of birth', disabled=True)
    school = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), label='', choices=SELECT_SCHOOL, disabled=True)
    year = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), label='', choices=SELECT_YEAR)
    semester = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), label='', choices=SELECT_SEMESTER)

    class Meta:
        model = Voters
        fields = '__all__'
