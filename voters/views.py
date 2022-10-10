from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, Logoutview
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import LoginForm, SignupForm

class VoterLogin(LoginView):
    authentication_form = LoginForm
    template_name = 'voters/login.html'


def signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_voter = form.save(commit=False)
            new_voter.username = new_voter.first_name+' '+new_voter.last_name
            new_voter.save()

            messages.success(request, 'New account created successfully!')
            return redirect('voter_profile')

    context = {'signup_form': form}
    return render(request, 'voters/signup.html', context)

@login_required(login_url='voters_login')
def votersprofile_view(request):
    form = ProfileForm()

    if request.method == 'POST':
        pass


    context = {}
    return render(request, 'voters/profile.html', context)


class LogoutVoter(LogoutView):
    template_name = 'voters/logout.html'