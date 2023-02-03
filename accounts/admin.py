from django.contrib import admin
from .models import Voters

@admin.register(Voters)
class VotersTable(admin.ModelAdmin):
    list_display = ['voter', 'gender', 'school', 'reg_no', 'year']
    readonly_fields = ['gender', 'dob', 'age', 'school', 'reg_no', 'year', 'semester', 'phone_no']
    fields = ['gender', 'dob', 'age', 'phone_no', 'school', 'reg_no', 'year', 'semester']
