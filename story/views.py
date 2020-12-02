from django.shortcuts import render

from story.models import Story


def landing(request):
    context = {
        'title': "Home|Tell Us A Story",
        'stories': Story.objects.all(),
    }
    return render(request, 'story/landing.html', context)


def about(request):
    context = {
        'title': "About Us"
    }
    return render(request, 'story/about.html', context)


def contact(request):
    context = {
        'title': "Contact Us"
    }
    return render(request, 'story/contact.html', context)
