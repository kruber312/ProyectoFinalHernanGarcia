from django.shortcuts import render

def about(request):
    return render(request,"about.html")

def notfound(request,exception):
    context = {"mensajes": ["No hay paginas aun"]}
    return render(request, "error.html", context=context)