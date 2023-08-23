from django.shortcuts import render, redirect
from . models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()
    context = {'students':students}
    return render(request, 'pages/index.html', context)

def create(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        content = request.POST['content']
        student = Student.objects.create(name=name, age=age, content=content)
        student.save()
        return redirect('index')
    return render(request, 'pages/create.html')

def edit(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        content = request.POST['content']

        student = Student.objects.get(id=pk)
        student.name=name
        student.age=age
        student.content=content
        student.save()

        return redirect('index')
    context = {'student':student}
    return render(request, 'pages/edit.html', context)

def delete(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        return redirect('index')
    return render(request, 'pages/delete.html')