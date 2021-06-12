from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse
from tstvApp.forms import CustomUserCreationForm

def home(request):
    return redirect(request, '/')

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def register(request):
    if request.method == "GET":
        return render(
            request, "register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse("dashboard"))

def profile(request):
    return render(request, 'profile.html')

def edit(request):
    return render(request,'edit.html')

def friends(request):
    return render(request, 'friends.html')

def groups(request):
    return render(request, 'groups.html')

def pending(request):
    return render(request, 'pending.html')

def categories(request):
    return render(request, 'categories.html')

def random(request):
    return render(request, 'random.html')