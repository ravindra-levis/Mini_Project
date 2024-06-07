from django.shortcuts import render ,HttpResponse,redirect


def home(request):
    return render(request,'register.html')