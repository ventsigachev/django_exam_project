from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

from story.models import Story
from story.forms import ContactForm


def landing(request):
    context = {
        'title': "Welcome! Nice to Have You Here!"
    }
    return render(request, 'story/landing.html', context)


@login_required
def home(request):
    context = {
        'title': "Home|Tell Us A Story",
        'stories': Story.objects.all(),
    }
    return render(request, 'story/home.html', context)


def about(request):
    context = {
        'title': "About Us"
    }
    return render(request, 'story/about.html', context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            f_name = form.cleaned_data['first_name']
            l_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # send email
            send_mail(subject,
                      message,
                      email,
                      ['to@example.com'],
                      fail_silently=True,
                      )

            context = {
                'title': "Thank You",
                'f_name': f_name,
                'l_name': l_name,
            }
            return render(request, 'story/success.html', context)
    else:
        form = ContactForm()
    context = {
        'title': "Contact Us",
        'form': form,
    }
    return render(request, 'story/contact.html', context)
