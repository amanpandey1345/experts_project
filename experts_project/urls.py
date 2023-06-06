
from django.contrib import admin
from django.urls import path
from experts_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homesection, name="homesection"),
    path('courses/', views.courses, name="courses"),
    path('registration/', views.registration, name="registration"),
    path('about/', views.about, name="about"),
    path('enquiry/', views.enquiry, name="enquiry"),
]
