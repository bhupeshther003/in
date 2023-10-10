from django.shortcuts import render , redirect
from django.views import  View


def home_page(request):
    return render(request,"index.html")


def service_page(request):
    return render(request,"services.html")


def courses_page(request):
    return render(request,"course.html")


def contact_page(request):
    return render(request,"contact.html")
  
def aboutus_page(request):
    return render(request,"about.html")

def career_page(request):
    return render(request,"career.html")
  
def job_list_page(request):
    return render(request,"job_list.html")

def payments_page(request):
    return render(request,"payments.html")
  
def store_books_poadcast(request):
    return render(request,"bookspoadcast.html")
  

