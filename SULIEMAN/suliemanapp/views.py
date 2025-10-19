from django.shortcuts import render
 
def myname_view(request):
    return render(request, "myname.html")
 
def myclass_view(request):
    return render(request, "myclass.html")
 
def linke_view(request):
    return render(request, "linke.html")
 
 