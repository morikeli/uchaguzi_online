from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import LoginForm, SignupForm, VoterRegistrationForm, EditProfileForm, ElectoralPostApplicationForm
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
    update_form = VoterRegistrationForm(instance=request.user.voters)
    edit_form = EditProfileForm(instance=request.user.voters)

    if request.method == 'POST':
        update_form = VoterRegistrationForm(request.POST, request.FILES, instance=request.user.voters)
        edit_form = EditProfileForm(request.POST, request.FILES, instance=request.user.voters)
        
        if update_form.is_valid():
            voterprof = update_form.save(commit=False)
            
            voters_dob = str(voterprof.dob)
            get_VoterDob = datetime.strptime(voters_dob, '%Y-%m-%d')
            current_date = datetime.now()
            voters_age = current_date - get_VoterDob
            convert_votersAge = int(voters_age/365.25)
            voterprof.age = convert_votersAge
            
            if voterprof.age < 18:
                messages.warning(request, 'Voting is only eleigible to voters above 18yrs!')
            else:
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

@login_required(login_url='voters_login')
@user_passes_test(lambda user: user.is_staff is False)
def application_view(request):
    application_form = ElectoralPostApplicationForm()
    if request.method == 'POST':
        application_form = ElectoralPostApplicationForm(request.POST, request.FILES)
        
        if application_form.is_valid():
            form = application_form.save(commit=False)

            if form.aspirant.gender == 'Male' and form.post == 'Ladies Representative':
                messages.warning(request, 'Only females are eligible to vie for "LADIES REPRESENTATIVE" electoral post!')
            elif form.aspirant.year != 'Fourth Year' and form.post == 'President':
                messages.warning(request, 'Only fourth years can vie for the Presidential seat!')

            else:
                form.aspirant = request.user.voters

                form.save()
                messages.redirect(request, f'You are vying for {form.post} electoral post. Kindly submit your nomination form in time.')



    context = {}
    return render(request, 'voters/homepage.html', context)


class LogoutVoter(LogoutView):
    template_name = 'voters/logout.html'