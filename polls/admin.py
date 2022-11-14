from django.contrib import admin
from .models import Polls, Polled

@admin.register(Polls)
class Polls(admin.ModelAdmin):
    list_display = ['name', 'post', 'total_polls', 'percentage']

@admin.register(Polled)
class PolledList(admin.ModelAdmin):
    list_display = ['user_id', 'academic', 'general_rep', 'ladies_rep', 'treasurer', 'governor', 'president', 'polled']
