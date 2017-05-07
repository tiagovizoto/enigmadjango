from django.contrib import admin
from .models import Job, Candidaty
# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list_display = ['title','location','created','modified']
    search_fields = ['title','description','location']
    list_filter = ['created','modified']


class CandidatyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'join_date', 'job']
    search_fields = ['name', 'email']
    list_filter = ['join_date']

admin.site.register(Job, JobAdmin)
admin.site.register(Candidaty, CandidatyAdmin)