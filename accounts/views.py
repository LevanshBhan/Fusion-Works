from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .forms import VendorRegistrationForm, CustomerRegistrationForm, VehicleForm, ServiceTypeForm
from .models import Vendor, Customer, Vehicle, ServiceType, Booking

def vendor_register(request):
    if request.method == 'POST':
        form = VendorRegistrationForm(request.POST, request.FILES)  # Note request.FILES for certificate
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.password = make_password(form.cleaned_data['password'])
            vendor.save()
            messages.success(request, 'Registration successful. Waiting for admin approval.')
            return redirect('vendor_register_success')
    else:
        form = VendorRegistrationForm()
    return render(request, 'accounts/vendor_register.html', {'form': form})

def vendor_register_success(request):
    return render(request, 'accounts/vendor_register_success.html')

def customer_register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.password = make_password(form.cleaned_data['password'])
            customer.save()
            return redirect('customer_dashboard')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'accounts/customer_register.html', {'form': form})

@login_required
def vendor_dashboard(request):
    if not hasattr(request.user, 'vendor') or not request.user.vendor.is_approved:
        messages.error(request, 'Your account is not approved yet.')
        return redirect('login')
    
    vendor = request.user.vendor
    services = ServiceType.objects.filter(vendor=vendor)
    bookings = Booking.objects.filter(vendor=vendor)
    context = {
        'services': services,
        'bookings': bookings,
    }
    return render(request, 'accounts/vendor_dashboard.html', context)

@login_required
def add_service(request):
    if request.method == 'POST':
        form = ServiceTypeForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.vendor = request.user.vendor
            service.save()
            return redirect('vendor_dashboard')
    else:
        form = ServiceTypeForm()
    return render(request, 'accounts/add_service.html', {'form': form})