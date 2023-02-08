from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.dispatch import receiver
from .models import Voters, Officials
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


@receiver(pre_save, sender=Officials)
def generate_officer_id(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).upper().replace('-', '')[:15]

    try:
        if datetime.now().strftime('%Y-%m-%d %H:%M:%S') > instance.created.strftime('%Y-%m-%d %H:%M:%S'):
            officer_dob = str(instance.dob)
            get_OfficerDob = datetime.strptime(officer_dob, '%Y-%m-%d')
            current_date = datetime.now()
            officer_age = current_date - get_OfficerDob
            convert_OfficerAge = int(officer_age.days/365.25)
            instance.age = convert_OfficerAge
            
        else:
            officer_dob = str(instance.dob)
            get_OfficerDob = datetime.strptime(officer_dob, '%Y-%m-%d')
            current_date = datetime.now()
            officer_age = current_date - get_OfficerDob
            convert_OfficerAge = int(officer_age.days/365.25)
            instance.age = convert_OfficerAge
            
    except AttributeError:
        return


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff is False and instance.is_superuser is False:
            Voters.objects.create(voter=instance)
        
        elif instance.is_staff is True and instance.is_superuser is False:
            Officials.objects.create(officer=instance)

