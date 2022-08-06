import imp
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse

from home.models import Contact

# Create your views here.
def index(request):
    # return HttpResponse("This is home page.")
    context={"name":"vishal kumar singh","father": "Umesh singh"}
    return render(request,'index.html',context)

def about(request):
    return HttpResponse("This is about page.")

def contact(request):
    return render(request,'contact.html')

def farm_management_solution(request):
    return render(request,'farm_management_solution.html')

def farm_risk_assessment(request):
    return render(request,"farm_risk_assessment.html")
def scts(request):
    return render(request,"supply_chain_traceability_solution.html")
def farming(request):
    return render(request,'farming.html')
def seed_companies(request):
    return render(request,'seeds_companies.html')
def food_processing(request):
    return render(request,'food_processing.html')
def blogs(request):
    return render(request,'blogs.html')
def news(request):
    return render(request,"request.html")
def webinars(request):
    return render(request,'webinars.html')
def case_study(request):
    return render(request,"case_study.html")
def about(request):
    return render(request,'about.html')
def carrers(request):
    return render(request,'carrer.html')
def contact(request):
    print(request.method)
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,subject=subject,desc=desc)
        contact.save()
    return render(request,'contact.html')
