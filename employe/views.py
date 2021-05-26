from django.shortcuts import render, redirect
from employe.forms import EmployeCreateForm
from employe.models import Employe


# Create your views here.
# create employe

def create_employe(request):
    form = EmployeCreateForm()
    context = {}
    context["form"] = form
    if request.method == 'POST':
        form = EmployeCreateForm(request.POST)
        if form.is_valid():
            emp_name = form.cleaned_data.get("name")
            designation = form.cleaned_data.get("designation")
            salary = form.cleaned_data.get("salary")
            location = form.cleaned_data.get("location")
            email = form.cleaned_data.get("email")
            employe = Employe(name=emp_name, designation=designation, salary=salary, location=location, email=email)
            employe.save()
            print("employe saved")

            # print(emp_name,designation,salary,location,email)
            return redirect("listemp")
    return render(request, "employe/createemploye.html", context)

# list all employe
def list_employes(request):
    employes = Employe.objects.all()
    context = {}
    context["employes"] = employes
    return render(request, "employe/listemployes.html", context)


# view employe
def emp_detail(request, id):
    employe = Employe.objects.get(id=id)
    context = {}
    context["employe"] = employe
    return render(request, "employe/empdetail.html", context)


# update employe

def edit_employe(request, id):
    employe=Employe.objects.get(id=id)
    emp={
        "name":employe.name,
        "designation":employe.designation,
        "salary":employe.salary  ,
        "location":employe.location,
        "email":employe.email
    }
    form = EmployeCreateForm(initial=emp)

    context = {}
    context["form"] = form
    if request.method=="POST":
        form = EmployeCreateForm(request.POST)
        if form.is_valid():
            emp_name = form.cleaned_data.get("name")
            designation = form.cleaned_data.get("designation")
            salary = form.cleaned_data.get("salary")
            location = form.cleaned_data.get("location")
            email = form.cleaned_data.get("email")
            print(emp_name,designation,salary,location,email)
            employe.name=emp_name
            employe.designation=designation
            employe.salary=salary
            employe.location=location
            employe.email=email
            employe.save()
            return redirect("listemp")


    return render(request, "employe/editemp.html", context)


# delete a employe
def delete_emp(request,id):
    employe=Employe.objects.get(id=id)
    employe.delete()
    return redirect("listemp")