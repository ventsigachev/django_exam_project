from abc import ABC

from django.shortcuts import render
from django.core.mail import send_mail
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from story.models import Story
from story.forms import ContactForm


def landing(request):
    context = {
        'title': "Welcome! Nice to Have You Here!"
    }
    return render(request, 'story/landing.html', context)


# @login_required
# def home(request):
#     context = {
#         'title': "Home|Tell Us A Story",
#         'stories': Story.objects.all(),
#     }
#     return render(request, 'story/home.html', context)


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


# Class Based Views
class StoryListView(LoginRequiredMixin, UserPassesTestMixin, ListView, ABC):
    model = Story
    template_name = 'story/home.html'
    context_object_name = 'stories'
    extra_context = {'title': "Home|Tell Us A Story"}
    ordering = ['-date']

    # must implement test_func and inherit ABC, for UserPassesTestMixin to work
    def test_func(self):
        # should return true if have access, for UserPassesTestMixin to work
        if self.request.user.is_authenticated:
            return True
        else:
            return False


class StoryDetailView(LoginRequiredMixin, DetailView):
    model = Story


class StoryCreateView(LoginRequiredMixin, CreateView):
    model = Story
    fields = ['title', 'content']
    success_url = reverse_lazy('story home')
    extra_context = {'title': "Create Story"}

    # FORM VALIDATION METHOD
    # To get rid of integrity error(NOT NULL constraint),
    # because in form fields missing author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Story
    fields = ['title', 'content']
    success_url = reverse_lazy('story home')
    extra_context = {'title': "Update Story"}

    # FORM VALIDATION METHOD
    def form_valid(self, form):
        actual_author = form.instance.author
        form.instance.author = self.request.user
        # not to change story author, when superuser edits author's post
        if self.request.user.is_superuser:
            form.instance.author = actual_author
        return super().form_valid(form)

    # this function is needed for UserPassesTestMixin
    def test_func(self):
        # need to use class get.object() method, to get the object(story)
        # of the class StoryUpdateView, other ways story in if statement is None
        story = self.get_object()
        # should return true if author of the story is user who requested that post
        # for UserPassesTestMixin to work
        return True if story.author == self.request.user or self.request.user.is_superuser else False
        # and the result is http response 403 FORBIDDEN


class StoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView, ABC):
    model = Story
    success_url = reverse_lazy('story home')
    extra_context = {'title': "Delete Story"}

    # same function again
    def test_func(self):
        story = self.get_object()
        return True if story.author == self.request.user or self.request.user.is_superuser else False
        # should return True if author and user are identical, or user is admin
