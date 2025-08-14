from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib import messages
from .forms import StudentForm, RegisterForm

def index(request):
    return render(request,'index.html')

@login_required
# Create your views here.
def student_list(request):
    students=(Student.objects.all())
    return render(request,'studentlist.html',{'students':students})

#Create-add a new student to our database
@login_required
@staff_member_required
def add_student(request):
    form=StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request,'studentform.html',{'form':form})


#Update
@login_required
def update_student(request,pk):
    student=get_object_or_404(Student,pk=pk)
    form=StudentForm(request.POST or None,instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request,'studentform.html',{'form':form})

#delete
def delete_student(request,pk):
    student=get_object_or_404(Student,pk=pk)
    student.delete()
    return redirect('student_list')

#register
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_user')
    else:
            form=RegisterForm()
    return render(request,'register.html',{'form':form})
#login
def login_user(request):
    if request.method == 'POST':
         form=AuthenticationForm(data=request.POST)
         if form.is_valid():
            user=form.get_user()  #authenticated user
            login(request,user)
            return redirect('student_list')
         else:
              messages.error(request,"Invalid username or password")
    else:#get
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

#logout
def logout_user(request):
    logout(request)
    return redirect ('login_user')
