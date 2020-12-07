from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.forms import TellerRegistrationForm
from django.contrib import messages

# Create your views here.


def sign_up(request):
    if request.method == "POST":
        form = TellerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f" Hello, {username}! Your Account has been created! You are now able to SignIn.")
            return redirect('login')
    else:
        form = TellerRegistrationForm()
    context = {
        'title': "Sign Up",
        'form': form
    }

    return render(request, 'users/signup.html', context)


@login_required
def user_profile(request):

    context = {
        'title': "User Profile"
    }
    return render(request, 'users/user_profile.html', context)
