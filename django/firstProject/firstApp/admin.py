from django.contrib import admin

# Register your models here.
from firstApp.models import AccessRecords,Topic,Webpage

admin.site.register(AccessRecords)
admin.site.register(Topic)
admin.site.register(Webpage)
