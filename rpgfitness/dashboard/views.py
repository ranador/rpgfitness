from django.shortcuts import render, redirect
from .form import ContactForm
from django.core.files.storage import default_storage

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def about(request):
    return render(request, 'dashboard/about.html')

def update(request):
    # print("Request method:", request.method)
    # print("Content type:", request.content_type)
    # print("POST data:", request.POST)
    # print("FILES data:", request.FILES)
    # print("Headers:", request.headers)

    context = {'type': 'warning', 'message': 'No files uploaded', 'request': f'{request}'}
    if request.method == 'POST':
        files = request.FILES.getlist('files')

        uploaded_files = []
        for f in files:
            path = f'uploads/{f.name}'
            uploaded_files.append(path)
            default_storage.save(path, f)
        context = {'type': 'success', 'message': 'All files uploaded successfully', 'files': uploaded_files}
    return render(request, 'dashboard/update.html', context)

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