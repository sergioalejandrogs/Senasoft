from django.shortcuts import render
import os
from django.core.files.storage import FileSystemStorage

def multiples(request):
    repositorio = "app/function/repositorio/"
    
    fichero =  os.scandir(repositorio)
    ctx = {"Repositorio":fichero}
    return render(request, 'multiples.html',ctx)

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'upload.html')
