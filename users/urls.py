from django.urls import path
from django.contrib.auth import views as auth_views

from users import views


urlpatterns = [
    path('signup/', views.sign_up, name='user signup'),
    path('login/', auth_views.LoginView.as_view(extra_context={"title": "Sign In"}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html",
                                                  extra_context={"title": "Signed Out"}), name='logout'),
    path('profile/', views.user_profile, name='user profile'),
    path('profile/update/', views.profile_update, name='profile update'),
]
