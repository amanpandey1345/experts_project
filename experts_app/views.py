from django.shortcuts import render, redirect
from .forms import RegistraionFrom , EnquiryFom
from django.contrib import messages
from .models import Regisration, Enquiry



# Create your views here.

def index(request):
    return render(request, 'index.html')

def homesection(request):
    return render(request, 'homesection.html')

def courses(request):
    return render(request, "courses.html")

def registration(request):
    if request.method == "POST":
        registrationFom = RegistraionFrom(request.POST)
        if registrationFom.is_valid():
            nm = registrationFom.cleaned_data['Name']
            add = registrationFom.cleaned_data['Address']
            mo = registrationFom.cleaned_data['Number']
            em = registrationFom.cleaned_data['Email']
            cou = registrationFom.cleaned_data['Course']
            res_table = Regisration(Name=nm, Address=add, Number=mo, Email=em, Course=cou)
            res_table.save()
            messages.success(request, "Registration Successful...")
            return redirect('registration')

    else:
        registrationFom = RegistraionFrom()
    return render(request, 'registration.html', {'registrationForm' : registrationFom})
    
def about(request):
    return render(request, 'about.html')

def enquiry(request):
    if request.method == "POST":
        EnqFom = EnquiryFom(request.POST)
        if EnqFom.is_valid():
            nm = EnqFom.cleaned_data['Name']
            num = EnqFom.cleaned_data['Number']
            ciy = EnqFom.cleaned_data['City']
            cour = EnqFom.cleaned_data['Course']
            enq_table = Enquiry(Name=nm, Number=num, City=ciy, Course=cour)
            enq_table.save()
            messages.success(request, "Enquiry Send Successful...")
            return redirect('enquiry')
    else:
        EnqFom = EnquiryFom()
    return render(request, 'enquiry.html', {'EnquiryForm' : EnqFom})    

