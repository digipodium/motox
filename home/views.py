from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subscriber
from .forms import ProjectForm

# Create your views here.
def index_view(request):
    if request.method == 'POST':
        email = request.POST.get('subscriber')
        if email and len(email)>10 and email.find('@')>0:
            sub = Subscriber(email=email)
            sub.save()
            messages.success(request, 'You have been successfully subscribed.')
        else:
            messages.error(request, 'Please enter a valid email address.')
        return redirect('index')

    return render(request, 'home/index.html',)

def contact_view(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        # print(name, email, message, subject)
        if name and email and message:
            messages.success(request, 'Your message has been sent successfully.')
        elif not name:
            messages.error(request, 'Please enter your name.')
        elif not email:
            messages.error(request, 'Please enter your email.')
        elif not message:
            messages.error(request, 'Please enter your message.')
        return redirect('contact')
    return render(request, 'home/contact.html')

def dashboard_view(request):
    form = ProjectForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Your project has been successfully added.')
            return redirect('dashboard')
    ctx = {
        'form': form,
    }
    return render(request, 'home/dashboard.html', ctx)