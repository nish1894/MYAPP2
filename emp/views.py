from django.contrib import admin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp
# from .forms import EmpForm



# Create your views here.
def emp_home(request):
    emps = Emp.objects.all()
    return render(request, "emp/home.html", {
        'emps': emps
    })
    # return render(request, "emp/home.html",{})

def add_emp(request):

    if request.method == "POST":
        # data fetch
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        #validate
        e = Emp()
        e.name = emp_name
        e.emp_id = emp_id
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True

        # save the object
        e.save()

        return redirect("/emp/home/")

    # form = EmpForm()
    # return render(request, "emp/add_emp.html", {'form': form})

        # return HttpResponse("data fetched with emp_name: "+ emp_name+"  and emp department: "+emp_department)
        # return redirect("/emp/home/")


    return render(request, "emp/add_emp.html",{})




def delete_emp(request,emp_id):
    emp = Emp.objects.get(pk=emp_id)
    emp.delete()
    print("employee with emp_id: " + str(emp_id) + " deleted")
    return redirect("/emp/home/")

def update_emp(request,emp_id):

    emp = Emp.objects.get(pk=emp_id)
    return render(request, "emp/update_emp.html", {
        'emps': emp
    })

def do_update_emp(request,emp_id):

    if request.method == "POST":

        # data fetch
        emp_name = request.POST.get("emp_name")
        emp_id_temp = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        #validate
        e = Emp.objects.get(pk=emp_id)
        e.name = emp_name
        e.emp_id = emp_id_temp
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True

        # #delete old
        # emp = Emp.objects.get(pk=emp_id)
        # emp.delete()
        # save the object
        e.save()

        return redirect("/emp/home/")

