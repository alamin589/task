# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Add other URL patterns as needed
    path('social/', views.socialmediaview, name='social_media'),
    path('register/', views.register, name='register'),
    path('list/', views.userprofile_list, name='userprofile_list'),
    path('create/', views.userprofile_create, name='userprofile_create'),
    path('<int:pk>/update/', views.userprofile_update, name='userprofile_update'),
    path('<int:pk>/delete/', views.userprofile_delete, name='userprofile_delete'),
]
