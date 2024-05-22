from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method=="POST":
     a=int(request.POST["num1"])
     b= int(request.POST["num2"])
     return render(request, 'a4/result. html',{"res":a+b})
    return render(request, 'a4/home.html'),

def resume(request):
    if request.method=='POST':
      personal={}
      educational={}
      skills={}
      personal.update({"name":request.POST["name"],"age":request.POST["age"],"email":request.POST["email"],"date":request.POST["date"]
        })
      educational.update({"qualification":request.POST["qualification"]})
      skills.update({"Skills":request.POST["Skills"]})
      return render(request,'a4/display.html',{'personal':personal,'educational':educational, 'skills':skills})
    return render(request,'a4/resume.html',)

