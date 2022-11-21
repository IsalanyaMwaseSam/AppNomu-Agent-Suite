from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegForm
from django.contrib.auth import login, authenticate
from .models import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegForm(request.POST, request.FILES)
        if form.is_valid():
            upload = request.FILES['upload']
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            file_url = fss.url(file)
            form.save()
            return render(request,'main_app/base.html', {'file_url': file_url})
        else:
            print('Form is not valid')
            print(form.errors)
    else:
        form = RegForm()
    return render(request, 'accounts/register.html', {'form': form})

