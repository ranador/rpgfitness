from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, about, contact, update

# Define a list of url patterns
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('update/', update, name='update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)