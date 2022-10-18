from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Polled, Polls
from .forms import PollingForm

@login_required(login_url='voters_login')
@user_passes_test(lambda user: user.is_staff is False)
def polling_view(request):
    if request.method == 'POST':
        form = request.POST['vote']

        

    
    return render(request, 'voters/homepage.html')

@login_required(login_url='voters_login')
@user_passes_test(lambda user: user.is_staff is False)
def results_view(request):

    context = {}
    return render(request, 'voters/homepage.html', context)