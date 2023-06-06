from django import forms


class RegistraionFrom(forms.Form):
    Name = forms.CharField(max_length=50)
    Address = forms.CharField(max_length=100)
    Number = forms.IntegerField()
    Email = forms.EmailField()
    Course = forms.CharField(max_length=20)


class EnquiryFom(forms.Form):
    Name = forms.CharField(max_length=50)
    Number = forms.IntegerField()
    City = forms.CharField(max_length=50)
    Course = forms.CharField(max_length=15)