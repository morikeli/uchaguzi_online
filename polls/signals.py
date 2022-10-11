from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Polls, Polled
import uuid

@receiver(pre_save, sender=Polls)
def aspirant_polls(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:15]

@receiver(pre_save, sender=Polled)
def voters_polled(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:18]