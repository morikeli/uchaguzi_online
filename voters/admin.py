from django.contrib import admin
from .models import Voters, Aspirants, Blog, Voted

@admin.register(Voters)
class VotersTable(admin.ModelAdmin):
    list_display = ['voter', 'gender', 'school', 'reg_no', 'year']

@admin.register(Aspirants)
class AspirantsTable(admin.ModelAdmin):
    list_display = ['name', 'post', 'slogan', 'nominate']
    readonly_fields = ['alias', 'bio', 'post', 'slogan', 'pic', 'form', 'nominate',]

@admin.register(Blog)
class BlogTable(admin.ModelAdmin):
    list_display = ['blogger', 'message', 'written']

@admin.register(Voted)
class VotedTable(admin.ModelAdmin):
    list_display = ['id', 'academic', 'general_rep', 'ladies_rep', 'treasurer', 'governor', 'president']
