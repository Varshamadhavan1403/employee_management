from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from . models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q

def index(request):
    return render(request, 'emplapp/index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request, 'emplapp/view_all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=request.POST['salary']
        bonus=request.POST['bonus']
        phone=request.POST['phone']
        dept=request.POST['dept']
        role=request.POST['role']
        # hire_date=request.POST['hire_date']
        new_emp=Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id=dept, role_id=role, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully")
    elif request.method == 'GET':
        return render(request, 'emplapp/add_emp.html')
    else:
        return HttpResponse("An error occured! Cannot add employee")


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
   
    return render(request, 'emplapp/remove_emp.html',context)



def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
            print(emps)
        if dept:
            emps = emps.filter(dept__name__icontains = dept)

        if role:
            emps = emps.filter(role__name__icontains = role)
        context={
            'emps':emps
        }
        return render(request, 'emplapp/view_all_emp.html', context)
    
    elif request.method =='GET':    
        return render(request, 'emplapp/filter_emp.html')
    
    else:
        return HttpResponse("An Error Occured")

