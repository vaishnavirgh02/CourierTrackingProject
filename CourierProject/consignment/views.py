from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import ConsignmentRegisterForm, ConsignmentUpdateForm
from django.contrib import messages


# Create your views here.
def Index(request):
    return render(request, 'consignment/index.html')

def user_check(user):
    return user.groups.filter(name='staff').exists()

@user_passes_test(user_check)
def Dashboard(request):
    return render(request, 'consignment/dashboard.html')


@user_passes_test(user_check)
def Register(request):
    if request.method == "POST":
        form = ConsignmentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Your account was successfully created!')
            return redirect('dashboard')
    else:
        form = ConsignmentRegisterForm()
    return render(request, 'consignment/consignment-register.html',{'form': form})


@user_passes_test(user_check)
def UpdateTrackInfo(request):
    if request.method == "POST":
        form = ConsignmentUpdateForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Your account was successfully created!')
            return redirect('dashboard')
    else:
        form = ConsignmentUpdateForm()
    return render(request, 'consignment/update.html',{'form': form})


