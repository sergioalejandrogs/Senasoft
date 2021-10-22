from django.shortcuts import render
import os
# from django import "multiples.html"
# Create your views here.

def multiples(request):
    repositorio = "app/function/repositorio/"
    
    fichero =  os.scandir(repositorio)
    ctx = {"Repositorio":fichero}
    #     for fichero in ficheros:
    #         print(fichero.name)
    return render(request, 'multiples.html',ctx)

def individual(request,):
    return render(request, 'individual.html')

# def mostrar(request,):
#     repositorio = "identificadorDocumento/app/function/repositorio/"
#     for archivo in os.listdir(repositorio):
#         return render(request, archivo)