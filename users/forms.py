from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django import forms
from .models import Voters, Aspirants, Blog

class VoterRegistrationForm(forms.ModelForm):
    SELECT_GENDER = (
        (None, '-- Select your gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    SELECT_SCHOOL = (
        (None, '-- Select your school --'),
        ('School of Arts, Social Sciences and Business', 'School of Arts, Social Sciences and Business (SASSB)'),
        ('School of Education', 'School of Education (SE)'),
        ('School of Information, Communication & Media Studies', 'School of Information, Communication & Media Studies (INFOCOMS)'),
        ('School of Science, Agriculture & Environmental Science', 'School of Science, Agriculture & Environmental Science (SSAES)'),
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
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'mt-2 mb-2', 'placeholder': 'Enter your mobile no.'}), label='', )
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='', help_text='Enter your date of birth. Date format: MM/DD/YYYY e.g. 07/31/2022')
    school = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), label='', choices=SELECT_SCHOOL)
    reg_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'placeholder': 'Enter your Registration No.'}), label='')
    year = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), label='', choices=SELECT_YEAR)
    semester = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), label='', choices=SELECT_SEMESTER)

    class Meta:
        model = Voters
        fields = ['gender', 'dob', 'phone_no', 'school', 'reg_no', 'year', 'semester', 'profile_pic']

class EditProfileForm(forms.ModelForm):
    SELECT_GENDER = (
        (None, '-- Select your gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    SELECT_SCHOOL = (
        (None, '-- Select your school --'),
        ('School of Arts, Social Sciences and Business', 'School of Arts, Social Sciences and Business (SASSB)'),
        ('School of Education', 'School of Education (SE)'),
        ('School of Information, Communication & Media Studies', 'School of Information, Communication & Media Studies (INFOCOMS)'),
        ('School of Science, Agriculture & Environmental Science', 'School of Science, Agriculture & Environmental Science (SSAES)'),
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
        ('2', '2'),
    )
    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_GENDER, disabled=True)
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': ' mb-2'}), disabled=True)
    dob = forms.CharField(widget=forms.TextInput(attrs={'type': 'date', 'class': 'mb-2'}), label='Date of Birth', disabled=True)
    reg_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}), label='Reg. No.', disabled=True)
    school = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_SCHOOL, disabled=True)
    year = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), label='Year of Study', choices=SELECT_YEAR, disabled=True)
    semester = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_SEMESTER, disabled=True)

    class Meta:
        model = Voters
        fields = ['gender', 'dob', 'phone_no', 'school', 'reg_no', 'year', 'semester', 'profile_pic']

class ElectoralPostApplicationForm(forms.ModelForm):
    SELECT_ELECTORAL_POST = (
        (None, '-- Select electoral post --'),
        ('Academic Representative', 'Academic Representative'),
        ('General Academic Representative', 'General Academic Representative'),
        ('Ladies Representative', 'Ladies Representative'),
        ('Treasurer', 'Treasurer'),
        ('Governor', 'Governor'),
        ('President', 'President')
    )
    alias = forms.CharField(widget=forms.TextInput(attrs={'class': 'mb-2', 'placeholder': 'Enter your nickname (optional)'}), label='', required=False)
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'mb-2', 'placeholder': 'Type your manifesto...'}), label='')
    post = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), label='', choices=SELECT_ELECTORAL_POST)
    slogan = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'placeholder': 'What\'s your slogan?'}), label='', help_text='Slogan, e.g. "Yes we can!", "Tuchape kazi", "Equality.Transparency.Honest"')
    

    class Meta:
        model = Aspirants
        fields = ['alias', 'post', 'bio', 'slogan', 'pic']

class UploadNominationForm(forms.ModelForm):
    SELECT_ELECTORAL_POST = (
        (None, '-- Select electoral post --'),
        ('Academic Representative', 'Academic Representative'),
        ('General Academic Representative', 'General Academic Representative'),
        ('Ladies Representative', 'Ladies Representative'),
        ('Treasurer', 'Treasurer'),
        ('Governor', 'Governor'),
        ('President', 'President')
    )
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'mb-2'}), label='Your Manifesto',  disabled=True)
    post = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_ELECTORAL_POST, disabled=True)
    slogan = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}), label='Your slogan', disabled=True)
    form = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'mb-1'}), 
        help_text='Upload nomination form. <b> NB: Only ".doc", ".docx", ".odt", ".pdf" files can be uploaded.</b>', 
        validators=[FileExtensionValidator(['doc', 'docx', 'odt', 'pdf'])])
    
    class Meta:
        model = Aspirants
        fields = ['post', 'bio', 'slogan', 'form']


class BlogForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'mb-2', 'placeholder': "What's on your mind ..."}), label='')
    
    class Meta:
        model = Blog
        fields = ['message']