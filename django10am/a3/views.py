from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request,'a3/home.html')
def about (request):
    return render(request,'a3/about.html')
def menu (request):
    return render(request,'a3/menu.html')
def contact (request):
    return render(request,'a3/contact.html')
def base (request):
    return render(request,'a3/base.html')
