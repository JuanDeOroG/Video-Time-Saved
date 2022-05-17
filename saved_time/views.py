from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    
    return render(request,"index.html")


def enviado(request):
    if request.method == "POST":
        hours = request.POST.get("hours")
        minutes=request.POST.get("minutes")
        speed = request.POST.get("speed")

    if hours=="":
        saved= int(minutes) / float(speed)
        duracion = int(minutes)
        saved2 = duracion - saved
        porcentaje = 100*saved2/duracion
        hours=0

    else:
        duracion = ((int(hours) * 60)+int(minutes))
        saved=  duracion/ float(speed)
        saved2 = duracion - saved
        porcentaje = 100*saved2/duracion


        
    return render(request, "enviado.html",{"hours":hours,"minutes":minutes, "saved2":round(saved2,2),"porcentaje":round(porcentaje,2)})
