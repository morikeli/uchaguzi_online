from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Polled, Polls
from .forms import PollingForm

@login_required(login_url='voters_login')
@user_passes_test(lambda user: user.is_staff is False)
def polling_view(request):
    form = PollingForm()
    try:
        obj = Polls.objects.get(id=pk)
        if request.method == 'POST':
            form = PollingForm(request.POST, instance=obj)
            if form.is_valid():
                voter = form.save(commit=False)
                voter.total_polls += 1
                
                save_voter_details = Polled.objects.create(user_id=voter.id)
                save_voter_details.save()
                voter.save()

                messages.success(request, 'You polled for this candidate. Results will be released soon.')
                return redirect('')
    
    except Polls.DoesNotExist:
        return redirect('voters_homepage')
    
    context = {'polling_form': form}
    return render(request, 'polls/', context)

def results_view(request):

    context = {}
    return render(request, 'polls/', context)