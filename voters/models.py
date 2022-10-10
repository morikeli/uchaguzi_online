from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Voters(models.Model):
    voter = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=7, blank=False)
    phone_no = models.CharField(max_length=14, blank=False)
    age = models.PositiveIntegerField(default=0)
    dob = models.DateField(null=True)
    profile_pic = models.ImageField(upload_to='VotersDps/', default='default.jpg')
    school = models.CharField(max_length=30, blank=False)
    year = models.CharField(max_length=10, blank=False)
    semseter = models.CharField(max_length=10, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.voter.username}'

    def save(self, *args, **kwargs):
        super(Voters, self).save(*args, **kwargs)

        dp = Image.open(self.profile_pic.path)

        if dp.height > 400 and dp.width > 400:
            output_size = (350, 350)
            dp.thumbnail(output_size)
            dp.save(self.profile_pic.path)

    class Meta:
        verbose_name_plural = 'Voters'
        ordering = ['voter']


class Aspirants(models.Model):
    aspirant = models.ForeignKey(Voters, on_delete=models.CASCADE, editable=False)
    bio = models.TextField(blank=False)
    post = models.CharField(max_length=20, blank=False)
    slogan = models.CharField(max_length=50, blank=True)
    pic = models.ImageField(upload_to='Aspirant-Dps/', default='default.jpg')
    form = models.FileField(upload_to='Nomination-Forms/')
    nominate = models.BooleanField(default=False)
    votes = models.PositiveIntegerField(default=0)
    apply = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(Aspirants, self).save(*args, **kwargs)

        dp = Image.open(self.pic.path)
        if dp.height > 400 and dp.width > 400:
            output_size = (400, 400)
            dp.thumbnail(output_size)
            dp.save(self.pic.path)
    
    def __str__(self):
        return f'{self.aspirant.voter}'

    class Meta:
        verbose_name_plural = 'Aspirants'
        ordering = ['aspirant']
