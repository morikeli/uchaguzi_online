from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import LoginForm, SignupForm, UpdateProfileForm, EditProfileForm
from datetime import datetime

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
            return redirect('voters_profile')

    context = {'signup_form': form}
    return render(request, 'voters/signup.html', context)

@login_required(login_url='voters_login')
@user_passes_test(lambda user: user.is_staff is False)
def votersprofile_view(request):
    update_form = UpdateProfileForm(instance=request.user.voters)
    edit_form = EditProfileForm(instance=request.user.voters)

    if request.method == 'POST':
        update_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.voters)
        edit_form = EditProfileForm(request.POST, request.FILES, instance=request.user.voters)
        
        if update_form.is_valid():
            voterprof = update_form.save(commit=False)
            
            if datetime.strptime(str(voterprof.dob), '%Y-%m-%d') > datetime.now().strftime('%Y-%m-%d'):
                messages.error(request, f'INVALID DATE!! Current year is {datetime.now()} but you have provided year {voterprof.dob}.')

            else:
                if Voters.objects.filter(reg_no=voterprof.reg_no).exists():
                    messages.error(request, f'Reg. No. {update_form.reg_no} provided already exists. Please enter a valid registration number to proceed.')
                else:
                    update_form.save()
                    messages.success(request, 'Profile updated successfully!')
        
        elif edit_form.is_valid():
            edit_form.save()
            messages.info(request, 'You have edited your profile.')
            return redirect('voters_profile')

    context = {'UpdateProfileForm': update_form, 'EditProfileForm': edit_form}
    return render(request, 'voters/profile.html', context)


class LogoutVoter(LogoutView):
    template_name = 'voters/logout.html'