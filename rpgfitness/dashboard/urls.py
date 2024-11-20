from django.urls import path
from .views import index, about, contact

# Define a list of url patterns
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]