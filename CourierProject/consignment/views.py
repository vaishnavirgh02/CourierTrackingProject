from django.shortcuts import render, redirect
from .models import DeliveryProgress, Consignment
from django.contrib.auth.decorators import user_passes_test
from .forms import ConsignmentRegisterForm, ConsignmentUpdateForm
from django.contrib import messages


# Create your views here.
def Index(request):
    return render(request, 'consignment/index.html')

def About(request):
    return render(request, 'consignment/about.html')

def user_check(user):
    return user.groups.filter(name='staff').exists()

@user_passes_test(user_check)
def Dashboard(request):
    return render(request, 'consignment/dashboard.html', {'user': request.user})


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
            messages.success(request, f'Your account was successfully updated')
            return redirect('dashboard')
    else:
        form = ConsignmentUpdateForm()
    return render(request, 'consignment/update.html',{'form': form})


def ConsignmentTrack(request):
    if request.method == "POST" and request.POST['search'] != '':
        print(request.POST.get('search', False)) 
        form = DeliveryProgress.objects.filter(consignment_id = int(request.POST.get('search', False)))
        form_default = DeliveryProgress.objects.filter(consignment_id = int(request.POST.get('search', False))).first()
        print(form)
        return render(request, 'consignment/consignment-track.html', {'forms': form, 'form2': form_default })

    else:
        form = DeliveryProgress.objects.filter(consignment_id = 1 ).all()
        form_default = DeliveryProgress.objects.filter(consignment_id = 1 ).first()
        print(form)
        return render(request, 'consignment/consignment-track.html', {'forms': form, 'form2': form_default })
