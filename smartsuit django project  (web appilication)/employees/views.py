import random

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from employees.forms import *


def dashboard(request):
    employees = Employee.objects.all()
    suits = Suit.objects.all()
    context = {
        'employees': employees,
        'suits': suits,
    }
    return render(request, 'dashboard.html', context)


def employees(request):
    employees = Employee.objects.all()
    employee_form = Employee_Form()
    context = {
        'employee_form': employee_form,
        'employees': employees,
    }
    return render(request, 'employees.html', context)


def add_employee(request):
    data = dict()
    form = Employee_Form(request.POST)
    emp_id = request.POST.get('emp_id')
    employee = Employee.objects.filter(emp_id=emp_id)
    queryset = Employee.objects.all()
    if form.is_valid():
        if (employee.exists()):
            data['emp_exist'] = False
        else:
            form.save()
            data['emp_exist'] = True
            data['html'] = render_to_string('employee_details.html', {'employees': queryset})
    else:
        data['reason'] = False
    return JsonResponse(data)


def update_employee(request, id):
    context = {}
    obj = get_object_or_404(Employee, emp_id=id)
    form = Employee_Form(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/employees/")
    context["form"] = form
    return render(request, "update_employee.html", context)


def update_suit(request, id):
    context = {}
    obj = get_object_or_404(Available_Suit, suit_id=id)
    form = Suit_Update_Form(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/suit/")
    context["form"] = form
    return render(request, "update_suit.html", context)


def suit(request):
    suits = Suit.objects.all()
    available_suit = Available_Suit.objects.all()
    allocate_suit = Suit_Form()
    suit_add_form = Suit_Add_Form()
    context = {
        'suits': suits,
        'allocate_suit': allocate_suit,
        'suit_add_form': suit_add_form,
        'available_suit': available_suit,
    }
    return render(request, 'suit.html', context)


def add_suit(request):
    data = dict()
    form = Suit_Add_Form(request.POST)
    queryset = Available_Suit.objects.all()
    suit_id = request.POST.get('suit_id')
    if form.is_valid():
        if Available_Suit.objects.filter(suit_id=suit_id).exists():
            data['suit_exist'] = False
        else:
            form.save()
            data['suit_exist'] = True
            data['html'] = render_to_string('suit_details.html', {'available_suit': queryset})
    else:
        data['reason'] = False
    return JsonResponse(data)


def allocate_suit(request):
    data = dict()
    form = Suit_Add_Form(request.POST)
    suit_id = request.POST.get('suit_id')
    emp_id = request.POST.get('name')
    suit = Available_Suit.objects.get(id=suit_id)
    emp = Employee.objects.get(id=emp_id)
    suit.allocate_to = emp
    suit.save()

    suit_obj = Suit.objects.all()
    suit_obj.create(
        suit_id=suit,
        name=emp
    )

    queryset = Available_Suit.objects.all()
    data['html'] = render_to_string('suit_details.html', {'available_suit': queryset})
    data['reason'] = True
    data['emp'] = emp.name
    return JsonResponse(data)


def delete_suit(request):
    data = dict()
    id = request.POST.get('id')
    suit = Available_Suit.objects.get(suit_id=id)
    suit.delete()
    suits = Available_Suit.objects.all()
    data['html'] = render_to_string("suit_details.html", {'available_suit': suits})
    data['success'] = True
    return JsonResponse(data)


def delete_employee(request):
    data = dict()
    id = request.POST.get('id')
    employee = Employee.objects.get(emp_id=id)
    employee.delete()
    employees = Employee.objects.all()
    data['html'] = render_to_string("employee_details.html", {'employees': employees})
    data['success'] = True
    return JsonResponse(data)


def realtime_data(request):
    data = dict()
    temp = request.POST.get('temp')
    pres = request.POST.get('pres')
    meth = request.POST.get('meth')
    co = request.POST.get('co')
    hr = request.POST.get('hr')
    o2 = request.POST.get('o2')
    r_suit = Suit.objects.order_by("?").first()
    r_suit.temperature = temp
    r_suit.pressure = pres
    r_suit.Methane = meth
    r_suit.co = co
    r_suit.heart_rate = hr
    r_suit.oxygen = o2
    r_suit.save()
    suits = Suit.objects.all()
    employees = Employee.objects.all()
    data['html'] = render_to_string('dashboard_details.html', {'suits': suits, 'employees': employees})
    data['reason'] = True
    data['meth'] = meth
    data['co'] = co
    data['hr'] = hr
    data['o2'] = o2
    data['emp_name'] = r_suit.name.name
    data['emp_id'] = r_suit.suit_id.suit_id
    return JsonResponse(data)
