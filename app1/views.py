from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Employee, Manager
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
import datetime
from django.contrib.auth import logout


# Create your views here.

def home(request):
    return render(request, 'home.html')


# def registration(request, **kwargs):
#     if request.method == "POST":
#         f = UserCreationForm(request.POST)
#         if f.is_valid():
#             f.save(commit=True)
#             return redirect(loginn)
#         else:
#             return render(request, 'register.html', {'f': f})
#     else:
#         f = UserCreationForm()
#         return render(request, 'register.html', {'f': f})


def registration(request):
    if request.method == "POST":
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect(loginn)
        else:
            return render(request, 'register.html', {'f': f})
    else:
        f = UserCreationForm
        return render(request, 'register.html', {'f': f})


def loginn(request):
    if request.method == "POST":
        t1 = request.POST['t1']
        t2 = request.POST['t2']
        print(t1)
        print(t2)
        user = authenticate(username=t1, password=t2)
        login(request, user)
        return redirect(employee)
    else:
        return render(request, 'login.html')


@login_required
def employee(request):
    if request.method == 'POST':
        d1 = request.POST['t1']
        d2 = request.POST['t2']
        t1 = datetime.datetime.strptime(d1, '%Y-%m-%d')
        t2 = datetime.datetime.strptime(d2, '%Y-%m-%d')
        d = request.POST['t3']
        e = Employee.objects.create(employee_name=request.user, start_date=t1, end_date=t2, description=d)
        e.save()
        return render(request, 'home.html')

    else:
        print(request.user)
        # e=Employee.objects.get(employee_name=request.user)
        return render(request, 'employee.html')  # ,{'e':e})


@login_required
def manager(request):
    print(request.user)
    m = Employee.objects.all()
    print(m)
    return render(request, 'profile.html', {'m': m})

def status(request):
    try:
        e=Employee.objects.get(employee_name=request.user)
        return render(request, 'status.html', {'e': e})
    except:
        d="apply leave can check status"
        return render(request, 'status.html',{ 'd': d})



def leave(request, *args, **kwargs):
    i = kwargs.pop('t')
    if request.method == 'POST':
        d1 = request.POST['t1']
        d2 = request.POST['t2']
        d3 = request.POST['t']
        if int(d2) <= 0:
            raise Exception("enter correct days")
        elif int(d2) > 3:
            d3 = False
        em = Employee.objects.get(pk=d1)
        if em.leave_status==True:
            raise Exception("Already Approved")
        em.total_leaves=em.total_leaves-int(d2)
        em.leave_status = d3
        em.save()
        m = Manager.objects.create(manager_name=request.user, emp_name=em)
        m.save()
        return render(request, 'home.html',{})
    else:
        return render(request, 'leave.html', {'i': i})


def logout_view(request):
    logout(request)
    return render(request, 'home.html')
