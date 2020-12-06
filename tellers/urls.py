from django.urls import path
from django.contrib.auth import views as auth_views

from tellers import views


urlpatterns = [
    path('signup/', views.sign_up, name='teller signup'),
    path('login/', auth_views.LoginView.as_view(extra_context={"title": "Sign In"}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="tellers/logout.html",
                                                  extra_context={"title": "Signed Out"}), name='logout'),
    path('profile/', views.teller_profile, name='teller profile'),
]
