from django.contrib.auth.models import User
from django.db import models
from PIL import Image

class Voters(models.Model):
    id = models.CharField(max_length=15, primary_key=True, editable=False, unique=True)
    voter = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    gender = models.CharField(max_length=7, blank=False)
    phone_no = models.CharField(max_length=14, blank=False)
    age = models.PositiveIntegerField(default=0, editable=False)
    dob = models.DateField(null=True, blank=False)
    profile_pic = models.ImageField(upload_to='Voters-Dps/', default='default.png')
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


class Officials(models.Model):
    id = models.CharField(max_length=15, primary_key=True, editable=False, unique=True)
    officer = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    gender = models.CharField(max_length=7, blank=False)
    phone_no = models.CharField(max_length=14, blank=False)
    dob = models.DateField(null=True, blank=False)
    age = models.PositiveIntegerField(default=0, editable=False)
    profile_pic = models.ImageField(upload_to='Officials-Dps/', default='default.png')
    school = models.CharField(max_length=70, blank=False)
    role = models.CharField(max_length=25, blank=False)
    is_official = models.BooleanField(default=False, editable=False)
    registered = models.BooleanField(default=False, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.voter.username).title()}'

    def save(self, *args, **kwargs):
        super(Officials, self).save(*args, **kwargs)

        dp = Image.open(self.profile_pic.path)

        if dp.height > 400 and dp.width > 400:
            output_size = (400, 400)
            dp.thumbnail(output_size)
            dp.save(self.profile_pic.path)

    class Meta:
        verbose_name_plural = 'Electoral Officials'
        ordering = ['officer']

