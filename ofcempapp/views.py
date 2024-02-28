from django.shortcuts import render,HttpResponse
from ofcempapp.models import Employee , Role , Depertment
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,"index.html")

def all_emp(request):
    emp = Employee.objects.all()
    context = {
        'emps' : emp
    }
    print(context)
    return render(request,"all_emp.html",context)

def add_emp(request):
    if request.method == 'POST':
        print('post')
        first=request.POST["emp_first_name"]
        last=request.POST["emp_last_name"]
        sal=int(request.POST["emp_salary"])
        deptmnt=int(request.POST["emp_dept"])
        rol=int(request.POST["emp_role"])
        phn=int(request.POST["emp_phone"])
        bon=int(request.POST["emp_bonus"])

        new_emp=Employee(first_name=first,last_name=last, salary=sal, dept_id=deptmnt, bonus=bon, role_id=rol, phone=phn,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully")
    elif request.method == 'GET':
        return render(request,"add_emp.html")
        print('get')
    else:
        return HttpResponse("an exception occured!!")
    

def remove_emp(request):
    return render(request,"remove_emp.html")

def filter_emp(request):
    return render(request,"filter_emp.html")