from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name='home/index.html')),
    path('blog/',TemplateView.as_view(template_name='home/blog.html')),
    path('about/',TemplateView.as_view(template_name='home/about.html')),
    path('contact/',TemplateView.as_view(template_name='home/contact.html')),
    path('services/',TemplateView.as_view(template_name='home/services.html')),
    path('testimonial/',TemplateView.as_view(template_name='home/testimonial.html')),
    path('login/',TemplateView.as_view(template_name='accounts/login.html')),
    path('register/',TemplateView.as_view(template_name='accounts/register.html')),

]