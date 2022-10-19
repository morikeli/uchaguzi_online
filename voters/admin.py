from django.contrib import admin
from .models import Voters, Aspirants, Blog

@admin.register(Voters)
class VotersTable(admin.ModelAdmin):
    list_display = ['voter', 'gender', 'school', 'reg_no', 'year']

@admin.register(Aspirants)
class AspirantsTable(admin.ModelAdmin):
    list_display = ['name', 'post', 'slogan', 'nominate']

@admin.register(Blog)
class BlogTable(admin.ModelAdmin):
    list_display = ['blogger', 'message', 'written']