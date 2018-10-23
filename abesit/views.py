from django.shortcuts import render,render_to_response

from .models import Register

from .forms import RegisterForm

import random

import string

from django.views.decorators.csrf import csrf_protect

from django.shortcuts import redirect

from django.http import HttpResponse



def Home(request):

        return render_to_response('abesit/Home.html')

def registered(request):
    Codes = request.GET.get('Codes')
    return render(request,'abesit/registered.html',{'Codes':Codes})



@csrf_protect
def index(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():

            new_register = Register(Name=request.POST['Name'],Roll_No=request.POST['Roll_No'],CSI=request.POST['CSI'],Year=request.POST['Year'],Contact_No=request.POST['Contact_No'],Email=request.POST['Email'],College_Code=request.POST['College_Code'],Quiz=request.POST['Quiz'],Gaming=request.POST['Gaming'],Coding=request.POST['Coding'],Androiddevelopment=request.POST['Androiddevelopment'],Groupdiscussion=request.POST['Groupdiscussion'],Webdesigning=request.POST['Webdesigning'])
            new_register.save()
            data = Register.objects.filter(Roll_No=request.POST['Roll_No']).values('Roll_No')
            rol = {
                "rollnumber" : data
            }
            return render_to_response('abesit/registered.html',rol)

    else:
        form = RegisterForm()

    context = {'form':form}
    return render(request,'abesit/index.html',context)

