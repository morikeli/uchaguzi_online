from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.dispatch import receiver
from .models import Voters, Aspirants, Blog, Polls, Polled, Voted
from datetime import datetime
import uuid


@receiver(pre_save, sender=Voters)
def generate_voter_id(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:15]

    try:
        if datetime.now().strftime('%Y-%m-%d %H:%M:%S') > instance.created.strftime('%Y-%m-%d %H:%M:%S'):
            voters_dob = str(instance.dob)
            get_VoterDob = datetime.strptime(voters_dob, '%Y-%m-%d')
            current_date = datetime.now()
            voters_age = current_date - get_VoterDob
            convert_votersAge = int(voters_age.days/365.25)
            instance.age = convert_votersAge
            
        else:
            voters_dob = str(instance.dob)
            get_VoterDob = datetime.strptime(voters_dob, '%Y-%m-%d')
            current_date = datetime.now()
            voters_age = current_date - get_VoterDob
            convert_votersAge = int(voters_age.days/365.25)
            instance.age = convert_votersAge
    
    except AttributeError:
        return

@receiver(pre_save, sender=Aspirants)
def generate_aspirant_id(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:15]

@receiver(pre_save, sender=Blog)
def generate_blogId(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:15]

@receiver(pre_save, sender=Voted)
def generate_VotedId(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).upper().swapcase().replace('-', '')[:18]


@receiver(pre_save, sender=Polls)
def aspirant_polls(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:15]


@receiver(pre_save, sender=Polled)
def voters_polled(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:18]


@receiver(post_save, sender=User)
def profile_signal(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff is False and instance.is_superuser is False:
            Voters.objects.create(voter=instance)


@receiver(post_save, sender=Aspirants)
def nominated_candidate_poll(sender, instance, created, **kwargs):
    if created is False:
        if instance.nominate is True:
            try:
                Polls.objects.create(name=instance, post=instance.post)
            except IntegrityError:
                return