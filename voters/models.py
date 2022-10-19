from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Voters(models.Model):
    id = models.CharField(max_length=15, primary_key=True, editable=False, unique=True)
    voter = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    gender = models.CharField(max_length=7, blank=False)
    phone_no = models.CharField(max_length=14, blank=False)
    age = models.PositiveIntegerField(default=0, editable=False)
    dob = models.DateField(null=True, blank=False)
    profile_pic = models.ImageField(upload_to='VotersDps/', default='default.jpg')
    reg_no = models.CharField(max_length=14, blank=False)
    school = models.CharField(max_length=70, blank=False)
    year = models.CharField(max_length=12, blank=False)
    semester = models.CharField(max_length=1, blank=False)
    registered = models.BooleanField(default=False, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.voter.username).title()}'

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
    id = models.CharField(max_length=15, primary_key=True, editable=False, unique=True)
    name = models.OneToOneField(Voters, on_delete=models.CASCADE, editable=False)
    alias = models.CharField(max_length=25, blank=True)
    bio = models.TextField(blank=False)
    post = models.CharField(max_length=32, blank=False)
    slogan = models.CharField(max_length=50, blank=True)
    pic = models.ImageField(upload_to='Aspirant-Dps/', default='default.png')
    form = models.FileField(upload_to='Nomination-Forms/')
    nominate = models.BooleanField(default=False)
    votes = models.PositiveIntegerField(default=0)
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
