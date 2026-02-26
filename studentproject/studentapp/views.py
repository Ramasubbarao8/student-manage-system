from django.shortcuts import render,redirect
from .models import Student
# Create your views here.

def home(request):
    students=Student.objects.all()
    return render(request,'index.html',{'students':students})

def add_student(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        course=request.POST['course']

        Student.objects.create(
            name=name,
            email=email,
            course=course
        )
        return redirect('/')
    return render(request,'add.html')
    