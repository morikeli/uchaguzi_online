from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Voters
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
            convert_votersAge = int(voters_age/365.25)
            instance.age = convert_votersAge

        else:
            voters_dob = str(instance.dob)
            get_VoterDob = datetime.strptime(voters_dob, '%Y-%m-%d')
            current_date = datetime.now()
            voters_age = current_date - get_VoterDob
            convert_votersAge = int(voters_age/365.25)
            instance.age = convert_votersAge
    
    except AttributeError:
        return