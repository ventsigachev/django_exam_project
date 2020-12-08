from django.urls import path

from story import views
from story.views import StoryListView, StoryDetailView, StoryCreateView, StoryUpdateView, StoryDeleteView

urlpatterns = [
    path('', views.landing, name='story landing'),
    #   path('home/', views.home, name='story home'),
    path('home/', StoryListView.as_view(), name='story home'),
    path('story/<int:pk>/', StoryDetailView.as_view(), name='story detail'),
    path('story/create/', StoryCreateView.as_view(), name='story create'),
    path('story/<int:pk>/update/', StoryUpdateView.as_view(), name='story update'),
    path('story/<int:pk>/delete/', StoryDeleteView.as_view(), name='story delete'),
    path('about/', views.about, name='story about'),
    path('contact/', views.contact, name='story contact'),
]
