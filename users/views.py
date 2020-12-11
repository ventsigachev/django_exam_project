from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.forms import TellerRegistrationForm, ProfileUpdateForm, UserUpdateForm
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
        'title': "User Profile",
    }
    return render(request, 'users/user_profile.html', context)


@login_required
def profile_update(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your Profile has been updated!')
            return redirect('user profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
        u_form = UserUpdateForm(instance=request.user)

    context = {'p_form': p_form,
               'u_form': u_form,
               'title': "Update Profile"
               }
    return render(request, 'users/profile_update.html', context)
