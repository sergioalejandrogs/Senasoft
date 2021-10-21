from django.shortcuts import render
# from django import "multiples.html"
# Create your views here.

def multiples(request):
    return render(request, 'multiples.html')

def individual(request,):
    return render(request, 'individual.html')

    