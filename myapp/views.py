import datetime

from django.http import HttpResponse
import datetime

from django.shortcuts import render


def test(request):
    date = datetime.datetime.now()

    return HttpResponse("<h1> Hello this is index page</h1>" + str(date))

def home(request):

    isActive = False
    name = "Nishant K"

    if request.method == "POST":

        inputName = request.POST.get('inputName')

        check = request.POST.get("check")
        print(inputName,check)


        if check is None:isActive = False
        else:isActive = True



    date = datetime.datetime.now()


    list_of_programs = [
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime numbers from 1 to 100',
        'WAP to print pascals triangle'
    ]
    student = {
        'student_name': "Mehul",
        'student_college': "NIT",
        'student_city': 'jaipur'
    }

    data = {
        'date': date,
        'isActive': isActive,
        'name': name,
        'list_of_programs': list_of_programs,
        'student_data': student
    }

    return render(request,"home.html",data)

def about(request):
    return render(request,"about.html",{})

def services(request):
    return render(request,"services.html",{})