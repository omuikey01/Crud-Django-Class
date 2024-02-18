from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    allobjects =  Registration.objects.all()
    return render(request, "index.html", {"data" : allobjects})

def formsave(request):
    if request.method == 'GET':
        name = request.GET['name']
        email = request.GET['email']
        patch = request.GET['patch']
        course = request.GET['course']
        fees = request.GET['fees']

        Registration.objects.create(name = name,
                                    email = email,
                                    batch = patch,
                                    course = course,
                                    fees = fees)

        allobjects =  Registration.objects.all()
        return render(request, "index.html", {"data" : allobjects})
    else :
        print("Nhi Mila ")


def show(request) :
    allobjects =  Registration.objects.all()
    return render(request, "index.html", {"data" : allobjects})


def editform(request, mil):
    print(mil)
    userdata = Registration.objects.get(id = mil)
    return render(request, "edit.html", {"data" : userdata})


def editformsave(request):
    if request.method == "POST":
        updateid = request.POST['idd']
        name = request.POST['name']
        email = request.POST['email']
        patch = request.POST['patch']
        course = request.POST['course']
        fees = request.POST['fees']

        member = Registration.objects.get(id=updateid)
        member.name = name
        member.email = email
        member.batch = patch
        member.course = course
        member.fees = fees
        member.save()
        allobjects =  Registration.objects.all()
        return render(request, "index.html", {"data" : allobjects})
    
def delete(request, id):
    data = Registration.objects.get(id=id)
    data.delete()
    allobjects =  Registration.objects.all()
    return render(request, "index.html", {"data" : allobjects})