from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Polled, Polls
from voters.models import Aspirants

@login_required(login_url='voters_login')
@user_passes_test(lambda user: user.is_staff is False)
def polling_view(request):
    if request.method == 'POST':
        form = request.POST['vote']

        if Polled.objects.filter().exists():
            return redirect('')
        else:
            elected_aspirant = Polls.objects.get(id=form)
            elected_aspirant.total_polls += 1
            elected_aspirant.save()

            
        

    context = {}
    return render(request, 'voters/homepage.html', context)

@login_required(login_url='voters_login')
@user_passes_test(lambda user: user.is_staff is False)
def results_view(request):

    context = {}
    return render(request, 'voters/homepage.html', context)