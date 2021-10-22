# Se renderiza 
from django.shortcuts import render
# Se importa la libreria os para mostrar  los archivo 
# del repositorio  en pantalla
import os
# Se creo una funcion para ver el multiples.html
def multiples(request):
    repositorio = "app/function/repositorio/"
    
    fichero =  os.scandir(repositorio)
    ctx = {"Repositorio":fichero}
    return render(request, 'multiples.html',ctx)


