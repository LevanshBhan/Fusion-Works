from django import forms
from .models import Vendor, Customer, Vehicle, ServiceType

class VendorRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Vendor
        fields = ['workshop_name', 'location', 'owner_name', 'contact_no', 
                 'certificate', 'email', 'password']
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

class CustomerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ['name', 'email', 'password']

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ['customer']

class ServiceTypeForm(forms.ModelForm):
    class Meta:
        model = ServiceType
        exclude = ['vendor']
