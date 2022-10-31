from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import (
    LoginForm, SignupForm, VoterRegistrationForm, EditProfileForm, ElectoralPostApplicationForm, UploadNominationForm,
    BlogForm
    )
from .models import Voters, Aspirants, Blog
from polls.models import Polled, Polls
from datetime import datetime


def indexpage_view(request):
    nominated_aspirants_sch = Aspirants.objects.filter(nominate=True).all().order_by('post')
    if request.user.is_authenticated:
        nominated_aspirants_sch = Aspirants.objects.filter(nominate=True, name__school=request.user.voters.school).all().order_by('post')

    nom_aspirants = Aspirants.objects.filter(nominate=False).all()

    context = {
        'nominated_aspirants': nom_aspirants, 'nominatedAspirants_CurrentUser': nominated_aspirants_sch,
        'TotalNominatedAspirants': Aspirants.objects.filter(nominate=True).count(),
        'TotalRegisteredVoters': Voters.objects.filter(registered=True).count(),
        'TotalAspirants': Aspirants.objects.all().count(),
        }
    return render(request, 'index.html', context)

def page404_view(request):
    return render(request, 'page404.html')

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
    voterregist_form = VoterRegistrationForm(instance=request.user.voters)
    edit_form = EditProfileForm(instance=request.user.voters)
    
    if request.method == 'POST':
        voterregist_form = VoterRegistrationForm(request.POST, request.FILES, instance=request.user.voters)
        edit_form = EditProfileForm(request.POST, request.FILES, instance=request.user.voters)
        
        if voterregist_form.is_valid():
            profile_form = voterregist_form.save(commit=False)

            # Date input validation
            voters_dob = str(profile_form.dob)
            get_VoterDob = datetime.strptime(voters_dob, '%Y-%m-%d')
            current_date = datetime.now()
            voters_age = current_date - get_VoterDob
            convert_votersAge = int(voters_age.days/365.25)
            profile_form.age = convert_votersAge
            
            if str(datetime.strptime(voters_dob, '%Y-%m-%d').strftime('%Y')) > str(datetime.now().strftime('%Y')):
                messages.error(request, f'INVALID DATE!! Current date is {datetime.now().strftime("%d-%m-%Y")} but you have provided date "*** {profile_form.dob.strftime("%d-%m-%Y")} ***".')
            
            elif profile_form.age < 18:
                    messages.warning(request, 'Voting is only eligible to voters above 18yrs!')

            else:
                if Voters.objects.filter(reg_no=profile_form.reg_no).exists():
                    messages.error(request, f'Reg. No. {profile_form.reg_no} provided already exists. Please enter a valid registration number to proceed.')
                else:
                    profile_form.registered = True
                    profile_form.save()
                    messages.success(request, 'Profile updated successfully!')
                    return redirect('voters_profile')
        
        elif edit_form.is_valid():
            edit_form.save()
            messages.info(request, 'You have edited your profile.')
            return redirect('voters_profile')

    context = {'UpdateProfileForm': voterregist_form, 'EditProfileForm': edit_form}
    return render(request, 'voters/profile.html', context)


@login_required(login_url='voters_login')
@user_passes_test(lambda user: user.is_staff is False)
@user_passes_test(lambda user: user.voters.registered is True)
def homepage_view(request):
    blog_form = BlogForm()
        
        
    if request.method == 'POST':
        blog_form = BlogForm(request.POST)

        if blog_form.is_valid():
            form = blog_form.save(commit=False)
            form.blogger = request.user.voters.aspirants
            form.save()
            messages.info(request, 'Blog uploaded successfully!')
            return redirect('voters_homepage')
    
    try:
        polled_obj = Polled.objects.get(user_id=request.user.voters.id)
    except Polled.DoesNotExist:
        polled_obj = ''

    registered_voters = Voters.objects.filter(registered=True, school=request.user.voters.school)
    pollers = Polled.objects.all().count()
    polls = Polls.objects.filter(name__name__school=request.user.voters.school).all().order_by('post', 'total_polls')
    total_aspirants = Aspirants.objects.filter(name__school=request.user.voters.school).count()
    blogs = Blog.objects.filter(blogger__name__school=request.user.voters.school, ).all().order_by('-written')
    polls_percentage = (pollers/registered_voters.count())*100

    context = {
        'blog_form': blog_form,
        'blogs': blogs, 'total_aspirants': total_aspirants, 'total_reg_voters': registered_voters.count(),
        'polled': pollers, 'user_has_polled': polled_obj, 'polls': polls, 'percentage': polls_percentage,
        'nominated': Aspirants.objects.filter(nominate=True, name__school=request.user.voters.school),
        'male_reg_voters': registered_voters.filter(registered=True, gender='Male', school=request.user.voters.school).count(),
        'female_reg_voters': registered_voters.filter(registered=True, gender='Female', school=request.user.voters.school).count(),
        'TotalRegVoters': Voters.objects.filter(school=request.user.voters.school, registered=True).all(),
    }    
    return render(request, 'voters/homepage.html', context)

@login_required(login_url='voters_login')
@user_passes_test(lambda user: user.is_staff is False)
def electoralpost_view(request, id, aspirant_name):
    nomination_form = UploadNominationForm()
    contest_form = ElectoralPostApplicationForm()
    try:
        nomination_form = UploadNominationForm(instance=request.user.voters.aspirants)
        if request.method == 'POST':
            nomination_form = UploadNominationForm(request.POST, request.FILES, instance=request.user.voters.aspirants)
            if nomination_form.is_valid():
                nomination_form.save()
                messages.success(request, 'Nomination form uploaded successfully!')
                return redirect('voters_vie', id, aspirant_name)
    
    except Aspirants.DoesNotExist:
        if request.method == 'POST':
            contest_form = ElectoralPostApplicationForm(request.POST, request.FILES)

            if contest_form.is_valid():
                form = contest_form.save(commit=False)
                
                # electoral posts validation
                if form.post == 'Ladies Representative' and request.user.voters.gender == 'Male':
                    messages.error(request, 'Only ladies are eligible to vie for the ladies representative seat.')
                    
                elif form.post == 'President' and request.user.voters.year != 'Fourth Year':
                    messages.error(request, 'Only fourth years can contest for the Presidential seat!')
                else:
                    form.name = request.user.voters
                    form.save()
                    if form.post == 'President':
                        messages.success(request, 'You are vying for the "Presidential" seat. Kindly submit your nomination form in time.')
                    elif form.post == 'Governor':
                        messages.success(request, 'You are vying for the "Gubernatorial" seat. Kindly submit your nomination form in time.')
                    else:
                        messages.success(request, f'You are vying for {form.post} electoral seat. Kindly submit your nomination form in time.')
                    return redirect('voters_vie', id, aspirant_name)


    context = {'application_form': contest_form, 'nomination_form': nomination_form}
    return render(request, 'voters/aspirant.html', context)

class LogoutVoter(LogoutView):
    template_name = 'voters/logout.html'