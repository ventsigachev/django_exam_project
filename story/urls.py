from django.urls import path

from story import views

urlpatterns = [
    path('', views.landing, name='story landing'),
    path('about/', views.about, name='story about'),
    path('contact/', views.contact, name='story contact'),
]
