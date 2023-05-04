from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Person
from .models import Qrcode

def index(request):
    return render(request, 'index.html')

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method =='POST':
        username= request.POST['username']
        password= request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('new')
        else:
            messages.info(request, 'Credential Invalid')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method =='POST':
        username = request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2 = request.POST['password2']
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.infco(request,'Username already Exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info("Password not the same")
            return redirect('register')

    else:
        return render(request,'register.html')

def new(request):
    if request.method=="POST":
        username = request.POST["username"]
        name = request.POST["name"]
        mobile = request.POST["mobileno"]
        email = request.POST["email"]
        city = request.POST["city"]
        skill1 = request.POST["skill1"]
        skill2 =request.POST["skill2"]
        skill3=request.POST["skill3"]
        post=request.POST["post"]
        we1=request.POST["we1"]
        we2=request.POST["we2"]
        we3= request.POST["we3"]
        des1=request.POST["des1"]
        des2=request.POST["des2"]
        des3=request.POST["des3"]
        eq= request.POST["eq"]
        selfdesc=request.POST["selfdesc"]
        new_person = Person(username=username, name=name, mobile=mobile, email=email, city=city,skill1=skill1,skill2=skill2,skill3=skill3,post=post,we1=we1,we2=we2,we3=we3,des1=des1,des2=des2,des3=des3,eq=eq,selfdesc=selfdesc)
        new_person.save()
        return redirect('templ')
    return render(request,'new.html')

def res(request):
    persons = Person.objects.all()
    return render(request,'res.html',{"persons":persons})

def templ(request):
    return render(request,'templ.html')

def res2(request):
    persons = Person.objects.all()
    return render(request,'res2.html',{"persons":persons})

def res3(request):
    persons = Person.objects.all()
    return render(request,'res3.html',{"persons":persons})

def res4(request):
    persons = Person.objects.all()
    return render(request,'res4.html',{"persons":persons})



def logout(request):
    auth.logout(request)
    return redirect('/')

def mydata(request):
    persons = Person.objects.all()
    return render(request, 'mydata.html',{"persons":persons})

def delete(request, id):
  person = Person.objects.get(id=id)
  person.delete()
  return render(request, 'delete.html')

def mydata2(request):
    
    persons = Person.objects.all()
    return render(request, 'mydata2.html',{"persons":persons})

def newss(request):
    if request.method =="POST":
        qrf = request.POST["qr"]
        qrcode = Qrcode(qrs = qrf)
        qrcode.save()
        return redirect('newss')
    return render(request, 'newss.html')


def template1(request):
    persons = Person.objects.all()
    return render(request,'template1.html',{"persons":persons})