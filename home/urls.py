from django.urls import path
from django.views.generic import TemplateView
from .views import *
urlpatterns = [
    path('', index_view, name='index'),
    path('blog/',TemplateView.as_view(template_name='home/blog.html')),
    path('about/',TemplateView.as_view(template_name='home/about.html')),
    path('contact/', contact_view, name='contact'),
    path('services/',TemplateView.as_view(template_name='home/services.html')),
    path('testimonial/',TemplateView.as_view(template_name='home/testimonial.html')),
    path('login/',TemplateView.as_view(template_name='accounts/login.html')),
    path('register/',TemplateView.as_view(template_name='accounts/register.html')),

]