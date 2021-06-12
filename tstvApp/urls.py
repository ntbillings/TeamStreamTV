from django.conf.urls import include, url
from django.urls import path     
from . import views
from tstvApp.views import dashboard, register

urlpatterns = [
    path('', views.dashboard),
    path('home', views.home),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('profile', views.profile),
    path('edit', views.edit),
    path('friends', views.friends),
    path('groups', views.groups),
    path('pending', views.pending),
    path('categories', views.categories),
    path('random', views.random),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^register/", register, name="register"),
]