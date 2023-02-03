from django.shortcuts import render
from django.contrib.auth.models import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .forms import LoginForm, SignupForm
from .models import Voters, Officials

def user_login_view(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user_account = auth.authenticate(username=username, password=password)

            if user_account is not None:
                officer = Officials.objects.filter(officer=username).exists()
                if officer is True:
                    if offcier.is_staff is True and officer.is_official is True:
                        auth.login(request, user_account)
                        return redirect('officials_homepage')

                elif Voters.objects.filter(voter=username).exists():
                    auth.login(request, user_account)
                    return redirect('voters_homepage')

                else:
                    messages.error(request, 'INVALID CREDENTIALS!!')
                    return redirect('user_login')
    

    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def voters_signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_voter = form.save(commit=False)
            new_voter.username = new_voter.first_name + ' ' + new_voter.last_name
            new_voter.save()

            messages.success(request, 'User account created successfully!')
            return redirect('voters_profile')

    context = {'signup_form': form}
    return render(request, 'accounts/signup.html', context)


def officials_signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_official_account = form.save(commit=False)
            new_official_account.username = new_official_account.first_name + ' ' + new_official_account.last_name
            new_official_account.save()

            messages.success(request, 'Electoral official account created successfully!')
            return redirect('official_profile')

    context = {'signup_form': form}
    return render(request, 'accounts/officials-signup.html', context)

class LogoutUser(LogoutView):
    template_name = 'accounts/logout.html'