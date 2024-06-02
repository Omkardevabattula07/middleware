from django.shortcuts import render

# Create your views here.
def manual_view(request):
    return render(request,"manual.html")
def restrict_view(request):
    return render(request,"restrict.html")