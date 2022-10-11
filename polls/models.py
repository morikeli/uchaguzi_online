from django.db import models
from voters.models import Aspirants, Voters


class Polls(models.Model):
    id = models.CharField(max_length=15, primary_key=True, editable=False)
    name = models.OneToOneField(Aspirants, on_delete=models.CASCADE, editable=False)
    total_polls = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        return super(Polls, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Polls'
        ordering = ['total_polls']

class Polled(models.Model):
    id = models.CharField(max_length=15, editable=False, primary_key=True, unique=True)
    user_id = models.CharField(max_length=20)
    polled = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        return super(Polled, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Polled'
