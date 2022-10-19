from django.db import models
from voters.models import Aspirants


class Polls(models.Model):
    id = models.CharField(max_length=15, primary_key=True, editable=False)
    name = models.OneToOneField(Aspirants, on_delete=models.CASCADE, editable=False)
    post = models.CharField(max_length=32, blank=False, editable=False)
    total_polls = models.PositiveIntegerField(default=0, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.name).title()}'

    def save(self, *args, **kwargs):
        return super(Polls, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Polls'
        ordering = ['-total_polls']

class Polled(models.Model):
    id = models.CharField(max_length=18, editable=False, primary_key=True, unique=True)
    user_id = models.CharField(max_length=20, editable=False)
    academic = models.BooleanField(default=False, blank=False, editable=False)
    general_rep = models.BooleanField(default=False, editable=False)
    ladies_rep = models.BooleanField(default=False, editable=False)
    treasurer = models.BooleanField(default=False, editable=False)
    governor = models.BooleanField(default=False, editable=False)
    president = models.BooleanField(default=False, editable=False)
    polled = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user_id}'

    def save(self, *args, **kwargs):
        return super(Polled, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Polled'
