from django.contrib import admin

# Register your models here.
from testlist.models import *

class subAdmin(admin.ModelAdmin):
	list_display = ('newIp','firstName','lastName','emailAddress',)
	search_fields = ['newIp','emailAddress','firstName','lastName']

admin.site.register(Submission,subAdmin)
