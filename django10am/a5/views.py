from django.shortcuts import render
from .forms import userform

# Create your views here.
def home (request):
    if request.method=="POST":
        fm=userform(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data)
            print("valid form")
        else:
            print("invaild form")
        return render(request,'a5/home.html')
    else:
        fm=userform()
        return render(request,'a5/home.html')             