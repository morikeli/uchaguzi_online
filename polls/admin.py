from django.contrib import admin
from .models import Polls, Polled

@admin.register(Polls)
class Polls(admin.ModelAdmin):
    list_display = ['name', 'total_polls']

@admin.register(Polled)
class PolledList(admin.ModelAdmin):
    list_display = ['user_id', 'polled']
