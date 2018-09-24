from django.contrib import admin
from navigation.models import Section

# Register your models here.

class SectionAdmin(admin.ModelAdmin):
        list_display = ('name','loc')
admin.site.register(Section,SectionAdmin)
