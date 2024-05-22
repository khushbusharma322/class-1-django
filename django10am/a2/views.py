from django.shortcuts import render

# Create your views here.
def home (request):
    return render (request,'a2/home.html',{'res':'0','display': False})
def addnum (request):
    x=int(request.GET["num1"])
    y=int(request.GET["num2"])
    print(x+y)
    return render(request,'a2/home.html',{'res':x+y,'display':True})