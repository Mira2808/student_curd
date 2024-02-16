from django.shortcuts import render,HttpResponse
from . models import Student
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.http import HttpResponse


def index(request):
    return render(request,'index.html')
def add(request):
     
    if request.method == "POST":
         username=request.POST.get('username')
         first_name=request.POST.get('first_name')
         last_name=request.POST.get('last_name')
         faname=request.POST.get('faname')
         phoneno=request.POST.get('phoneno')
         email=request.POST.get('email')
         classno=request.POST.get('classno')
         cteacher=request.POST.get('cteacher')
        
         user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email)
         student=Student(faname=faname,phoneno=phoneno,classno=classno,cteacher=cteacher,user_model=user)
         user.save()
         student.save()
         return redirect("index")
    return render(request,'add.html')


def edit(request):
     u_object=User.objects.all()
     stu_object=Student.objects.all()
     combined_objects = zip(u_object,stu_object)
     context={"combined_objects":combined_objects}
     return render(request,'edit.html',context=context)    

def editfrom(request,u_id):
        user_detail= User.objects.get(id=u_id)
        stu=Student.objects.get(user_model=user_detail.id)

        
        if request.method == "POST":
             username=request.POST.get('username')
             first_name=request.POST.get('first_name')
             last_name=request.POST.get('last_name')
             faname=request.POST.get('faname')
             phoneno=request.POST.get('phoneno')

             email=request.POST.get('email')
             classno=request.POST.get('classno')
             cteacher=request.POST.get('cteacher')

             user_detail.username=username
             user_detail.first_name=first_name
             user_detail.last_name=last_name
             stu.faname=faname
             stu.phoneno=phoneno
             user_detail.email=email
             stu.classno=classno
             stu.cteacher=cteacher

             user_detail.save()
             stu.save()
             return redirect("index")
        context={"user_detail":user_detail,"stu":stu}
        return render(request,'editfrom.html',context=context)

def show(request):
    u_object=User.objects.all()
    stu_object=Student.objects.all()
    combined_objects = zip(u_object,stu_object)
    context={"combined_objects":combined_objects}

    return render(request,'show.html',context=context)
   
def delete(request,u_id):
    d_obj=User.objects.get(id=u_id)
    if request.method=="POST":
         d_obj.delete()
         return redirect("edit")
    context={"d_obj":d_obj}
    return render(request,'delete.html',context=context)


  

