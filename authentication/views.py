from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import LoginForm, SignUpForm


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "you are logged in")
                return redirect("/")
            else:
                msg = 'Invalid credentials'
                messages.error(request, msg)
        else:
            msg = 'Error validating the form'
            messages.error(request, msg)
    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'Account created - please <a href="/login">login</a>.'
            success = True
            messages.success(request, msg)
            return redirect('authen:login')

        else:
            msg = 'Forms details are invalid'
            messages.error(request, msg)
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})