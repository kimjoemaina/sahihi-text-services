from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blog, name='blog'),
    path('blog/post/', views.post, name='post')
]