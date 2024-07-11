from django.shortcuts import render,HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages
 
# Create your views here.
context={
        "variable":"this is sent"
    }
def index(request):
    return render(request,'index.html',context)
    #return HttpResponse("this is home page.")

def about(request):
    return render(request,'about.html',context)
    #return HttpResponse("this is about page.")
    
def services(request):
    return render(request,'services.html',context)
    #return HttpResponse("this is a service page.")

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'Your messsage have been sent!!!')
        
    return render(request,'contacts.html',context)
    #return HttpResponse("this is a contact page.")