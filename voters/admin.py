from django.contrib import admin
from .models import Voters, Aspirants, Blog, Voted, Polls, Polled

@admin.register(Voters)
class VotersTable(admin.ModelAdmin):
    list_display = ['voter', 'gender', 'school', 'reg_no', 'year']
    readonly_fields = ['gender', 'dob', 'age', 'school', 'reg_no', 'year', 'semester', 'phone_no']
    fields = ['gender', 'dob', 'age', 'phone_no', 'school', 'reg_no', 'year', 'semester']

@admin.register(Aspirants)
class AspirantsTable(admin.ModelAdmin):
    list_display = ['name', 'post', 'slogan', 'nominate']
    readonly_fields = ['alias', 'bio', 'post', 'slogan', 'pic', 'form',]
    fields = ['alias', 'bio', 'post', 'slogan', 'pic', 'form', 'nominate']

@admin.register(Blog)
class BlogTable(admin.ModelAdmin):
    list_display = ['blogger', 'message', 'written']
    readonly_fields = ['message']

@admin.register(Voted)
class VotedTable(admin.ModelAdmin):
    list_display = ['id', 'academic', 'general_rep', 'ladies_rep', 'treasurer', 'governor', 'president', 'voted']
    ordering = ['-voted']

@admin.register(Polls)
class Polls(admin.ModelAdmin):
    list_display = ['name', 'post', 'total_polls', 'percentage']

@admin.register(Polled)
class PolledList(admin.ModelAdmin):
    list_display = ['user_id', 'academic', 'general_rep', 'ladies_rep', 'treasurer', 'governor', 'president', 'polled']
