from django.shortcuts import render

def inicio(request):
    titulo = "Inicio"
    nombre = "Mauricio Cuervo"
    context={
        "titulo": titulo,
        "nombre": nombre,
    } 
    return render(request, 'index.html', context)
