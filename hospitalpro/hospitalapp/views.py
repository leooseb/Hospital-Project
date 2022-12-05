from django.shortcuts import render
from .models import Department
from .models import Doctors
from.forms import BookingForm
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request,"index.html")

def contact(request):
    if request.method=="POST":
        form2demo=ContactForm(request.POST)
        if form2demo.is_valid():
            form2demo.save()
            return render(request,"remarks.html")
    myform2=ContactForm()
    dict_cont={
        'contkey':myform2
    }
    return render(request,"contact.html",dict_cont)

def booking(request):
    if request.method=="POST":
        formdemo=BookingForm(request.POST)
        if formdemo.is_valid():
            formdemo.save()
        return render(request,"confirm.html")
        
    myform1=BookingForm()
    dict_book={
        'formkey':myform1
    }
    return render(request,"booking.html",dict_book)
    
def doctor(request):
    dict_docs={
        'doctkey':Doctors.objects.all()
    }
    return render(request,"doctor.html",dict_docs)

def department(request):
    dict_dept={
        'deptkey':Department.objects.all()
    }
    return render(request,"department.html",dict_dept)

def about(request):
    return render(request,"about.html")