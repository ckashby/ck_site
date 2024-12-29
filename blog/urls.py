from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('posts', views.posts),
    path('posts/<slug:slug>', views.post_details), 
]
