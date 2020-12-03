from django.urls import path

from tellers import views


urlpatterns = [
    path('signup/', views.sign_up, name='teller signup'),
]
