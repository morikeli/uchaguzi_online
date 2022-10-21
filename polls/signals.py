from django.db.utils import IntegrityError
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Polls, Polled
from voters.models import Aspirants, Voters
import uuid

@receiver(pre_save, sender=Polls)
def aspirant_polls(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:15]
        

@receiver(pre_save, sender=Polled)
def voters_polled(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:18]

@receiver(post_save, sender=Aspirants)
def nominated_candidate_poll(sender, instance, created, **kwargs):
    if created is False:
        if instance.nominate is True:
            Polls.objects.create(name=instance, post=instance.post)

@receiver(post_save, sender=Polls)
def calculate_polls_percentage(sender, instance, created, **kwargs):
    total_voters = Voters.objects.filter(registered=True).count()
    instance.percentage = (instance.total_polls/total_voters)*100
    print(f'Percentage: {instance.percentage}')
    
