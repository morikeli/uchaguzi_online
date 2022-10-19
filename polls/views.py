from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Polled, Polls
from voters.models import Aspirants


@login_required(login_url='voters_login')
@user_passes_test(lambda user: user.is_staff is False)
@user_passes_test(lambda user: user.voters.registered is True)
def polling_view(request, pk, school):
    try:
        polled_obj = Polled.objects.get(user_id=pk)
        print(f'Object: {polled_obj}')
    except Polled.DoesNotExist:
        polled_obj = ''

    if request.method == 'POST':
        form = request.POST['vote']

        if Polled.objects.filter(user_id=request.user.voters).exists():
            return redirect('poll', pk, school)
        else:
            elected_aspirant = Polls.objects.get(id=form)
            elected_aspirant.total_polls += 1

            polled_user = Polled.objects.filter(user_id=pk).exists()
            if polled_user is True:
                if elected_aspirant.post == 'Academic Representative':
                    polled_obj.academic = True
                elif elected_aspirant.post == 'General Academic Representative':
                    polled_obj.general_rep = True
                elif elected_aspirant.post == 'Ladies Representative':
                    polled_obj.ladies_rep = True
                elif elected_aspirant.post == 'Treasurer':
                    polled_obj.treasurer = True
                elif elected_aspirant.post == 'Governor':
                    polled_obj.governor = True
                elif elected_aspirant.post == 'President':
                    polled_obj.president = True 
                polled_obj.save()   
            
            else:
                polling_user = Polled.objects.create(user_id=pk)
                if elected_aspirant.post == 'Academic Representative':
                    polling_user.academic = True
                elif elected_aspirant.post == 'General Academic Representative':
                    polling_user.general_rep = True
                elif elected_aspirant.post == 'Ladies Representative':
                    polling_user.ladies_rep = True
                
                polling_user.save()

            elected_aspirant.save()
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
