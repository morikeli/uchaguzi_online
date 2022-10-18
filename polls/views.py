from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Polled, Polls
from voters.models import Aspirants


@login_required(login_url='voters_login')
@user_passes_test(lambda user: user.is_staff is False)
@user_passes_test(lambda user: user.voters.registered is True)
def polling_view(request, pk, school):
    try:
        polled_obj = Polled.objects.get(user_id=request.user.voters.id)
    except Polled.DoesNotExist:
        polled_obj = ''


    if request.method == 'POST':
        form = request.POST['vote']

        if Polled.objects.filter().exists():
            return redirect('poll', pk, school)
        else:
            elected_aspirant = Polls.objects.get(id=form)
            elected_aspirant.total_polls += 1
            elected_aspirant.save()

            polling_user = Polled.objects.create(user_id=request.user.voters.voter.id)
            polling_user.save()

            return redirect('poll', pk, school)        


    nominated_aspirants = Polls.objects.all().order_by('post', 'name')
    
    context = {'aspirants': nominated_aspirants, 'UserhasPolled': polled_obj}
    return render(request, 'polls/polls.html', context)

@login_required(login_url='voters_login')
@user_passes_test(lambda user: user.is_staff is False)
def results_view(request):
    elected_aspirants = Polls.objects.all()

    context = {'polls': elected_aspirants,}
    return render(request, 'voters/homepage.html', context)
