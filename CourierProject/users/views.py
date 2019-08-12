from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfileRegisterForm
from django.contrib.auth.models import Group

def Register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, f'Your account was successfully created!')
            return redirect('login')
        else:
            messages.error(request, f'There was an error in creating your account')
    else:
        user_form = UserRegisterForm()
    return render(request, 'users/customer_register.html', {
        'user_form': user_form
    })

