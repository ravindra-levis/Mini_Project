from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import teacher_only

def home(request):
    return render(request,'register.html')

def handleSignup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if len(username) > 10:
            messages.error(request,"Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        group =Group.objects.get(name='student')
        myuser.groups.add(group)
        messages.success(request,"Account successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


def handleLogin(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']

        user=authenticate(username= loginusername, password= loginpass)
        if user is not None:
            login(request, user)
            messages.success(request,"Successfully Logged In")
            return redirect("branch")
        else:
            messages.error(request,"Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


@login_required
def branch(request):
    return render(request,"branch.html")

@login_required
def semester(request):
    return render(request,"semester.html")


# def upload(request):
#     context={}
#     if request.method =="POST":
#         uploaded_file=request.FILES['document']        
#         fs = FileSystemStorage()
#         name = fs.save(uploaded_file.name, uploaded_file)
#         context['url'] = fs.url(name)
#         print(context)
#         print(uploaded_file.size)
#     return render(request,'upload.html',context)

