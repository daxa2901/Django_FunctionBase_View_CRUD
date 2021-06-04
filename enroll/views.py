from django import http
from django.http.response import HttpResponseRedirect
from django.shortcuts import render , HttpResponse
from .forms import StudentRegistration
from .models import User
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            #use this 
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            fm = StudentRegistration()
            #you can also simply use fm.save()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()        
    return render(request, 'enroll/addandshow.html', {'form': fm , 'stu':stud})

def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()  
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
          
    return render(request, 'enroll/updatestudent.html', {'form':fm})


def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')