from django.db import models
from accounts.models import Voters, Officials
from PIL import Image

class Aspirants(models.Model):
    id = models.CharField(max_length=15, primary_key=True, editable=False, unique=True)
    name = models.OneToOneField(Voters, on_delete=models.CASCADE, editable=False)
    alias = models.CharField(max_length=25, blank=True)
    bio = models.TextField(blank=False)
    post = models.CharField(max_length=32, blank=False)
    slogan = models.CharField(max_length=50, blank=True)
    pic = models.ImageField(upload_to='Aspirant-Dps/', null=False)
    form = models.FileField(upload_to='Nomination-Forms/')
    nominate = models.BooleanField(default=False)
    votes = models.PositiveIntegerField(default=0, editable=False)
    applied = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(Aspirants, self).save(*args, **kwargs)

        dp = Image.open(self.pic.path)
        if dp.height > 400 and dp.width > 400:
            output_size = (400, 400)
            dp.thumbnail(output_size)
            dp.save(self.pic.path)
    
    def __str__(self):
        return f'{str(self.name.voter).title()}'

    class Meta:
        verbose_name_plural = 'Aspirants'
        ordering = ['name']


class Blog(models.Model):
    id = models.CharField(max_length=15, primary_key=True, editable=False)
    blogger = models.ForeignKey(Aspirants, on_delete=models.CASCADE, editable=False)
    message = models.TextField(blank=False)
    written = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Blogs'
        ordering = ['written']
    
    def __str__(self):
        return f'{self.message}'[:20]


class Polls(models.Model):
    id = models.CharField(max_length=15, primary_key=True, editable=False)
    name = models.OneToOneField(Aspirants, on_delete=models.CASCADE, editable=False)
    post = models.CharField(max_length=32, blank=False, editable=False)
    total_polls = models.PositiveIntegerField(default=0, editable=False)
    percentage = models.DecimalField(max_digits=4, decimal_places=1, default=0, editable=False)
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


class Voted(models.Model):
    id = models.CharField(max_length=18, editable=False, primary_key=True, unique=True)
    user_id = models.CharField(max_length=20, editable=False)
    academic = models.BooleanField(default=False, blank=False, editable=False)
    general_rep = models.BooleanField(default=False, editable=False)
    ladies_rep = models.BooleanField(default=False, editable=False)
    treasurer = models.BooleanField(default=False, editable=False)
    governor = models.BooleanField(default=False, editable=False)
    president = models.BooleanField(default=False, editable=False)
    voted = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user_id}'

    def save(self, *args, **kwargs):
        return super(Voted, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Voted'
        

# Table to store officer who has nominated a candidate
class NominationDetails(models.Model):
    id = models.CharField(max_length=15, primary_key=True, editable=False, unique=True)
    name = models.ForeignKey(Officials, on_delete=models.CASCADE, editable=False)
    gender = models.CharField(max_length=7, blank=False)
    officer_school = models.CharField(max_length=70, blank=False)
    role = models.CharField(max_length=25, blank=False)
    aspirant_name = models.ForeignKey(Aspirants, on_delete=models.CASCADE, editable=False)
    electoral_post = models.CharField(max_length=32, blank=False)
    aspirant_school = models.CharField(max_length=70, blank=False)
    has_nominated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Officer Nomination Details'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

