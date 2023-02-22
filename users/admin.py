from django.contrib import admin
from .models import Aspirants, Blog, Voted, Polls, Polled, NominationDetails


@admin.register(Aspirants)
class AspirantsTable(admin.ModelAdmin):
    list_display = ['name', 'post', 'slogan', 'nominate', 'approved']
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
@admin.register(NominationDetails)
class NominationDetailsTable(admin.ModelAdmin):
    list_display = ['officer_name', 'officer_school', 'role', 'aspirant_name', 'has_nominated']
    readonly_fields = ['officer_school', 'role', 'aspirant_name', 'has_nominated']

