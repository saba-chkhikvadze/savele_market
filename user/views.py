from user.forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid:
            new_user = form.save()
            messages.success(request, 'წარმატებით დარეგისტრირდით')
            login(request, new_user)
            return redirect('setup_profile')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'user/registration.html', context)
