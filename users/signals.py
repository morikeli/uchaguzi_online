from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.dispatch import receiver
from .models import Aspirants, Blog, Polls, Polled, Voted


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


@receiver(post_save, sender=Aspirants)
def nominated_candidate_poll(sender, instance, created, **kwargs):
    if created is False:
        if instance.nominate is True:
            try:
                Polls.objects.create(name=instance, post=instance.post)
            except IntegrityError:
                return