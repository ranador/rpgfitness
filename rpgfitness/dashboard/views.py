from django.shortcuts import render, redirect
from .form import ContactForm

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def about(request):
    return render(request, 'dashboard/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('index')
    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'dashboard/contact.html', context)