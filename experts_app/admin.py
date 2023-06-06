from django.contrib import admin
from .models import Regisration, Enquiry
# Register your models here.


@admin.register(Regisration)
class Regisration(admin.ModelAdmin):
    list_display = ['Name', 'Address', 'Number', 'Email', 'Course']

@admin.register(Enquiry)
class Enquiry(admin.ModelAdmin):
    list_display = ['Name', 'Number', 'City', 'Course'] 
