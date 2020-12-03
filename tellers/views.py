from django.shortcuts import render, redirect
from tellers.forms import TellerRegistrationForm
from django.contrib import messages

# Create your views here.


def sign_up(request):
    if request.method == "POST":
        form = TellerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Account created for teller {username}!")
            return redirect('story landing')
    else:
        form = TellerRegistrationForm()
    context = {
        'title': "Sign Up",
        'form': form
    }

    return render(request, 'tellers/signup.html', context)
