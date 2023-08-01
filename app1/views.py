from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.views import View
import logging

logger = logging.getLogger("django")

class Employee_view(View):

    def get(self,request):
        template_name = 'app1/employee.html'
        form = EmployeeForm()
        context = {"form":form}
        return render(request,template_name,context)
    
    def post(self,request):
        template_name = 'app1/employee.html'
        form = EmployeeForm(request.POST)
        if form.is_valid():

            form.save()
            logger.info("New record added")

            return redirect("show_url")
        context = {"form":form}
        return render(request,template_name, context)

class show_view(View):
    
    def get(self,request):
        template_name = 'app1/show.html'
        data = Employee.objects.all()
        #logger.info("All records are fetched and displyed on show page")
        logger.error("All records are fetch and displayed on show page ")
        context = {"data":data}
        return render(request,template_name,context)

class update_view(View):
    def get(self,request, pk):
        template_name = 'app1/employee.html'
        obj = Employee.objects.get(eid = pk)
        form = EmployeeForm(instance=obj)
        context = {"form":form}
        return render(request,template_name,context)
    
    def post(self, request, pk):
        template_name = 'app1/employee.html'
        obj = Employee.objects.get(eid=pk)
        form = EmployeeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            logger.info("Reacord is update")
            return redirect('show_url')
        context = {"form":form}
        return render(request,template_name,context)
    


class delete_view(View):
    def get(self,request, pk):
        template_name = 'app1/delete.html'
        return render(request,template_name)
    
    def post(self,request,pk):
        obj = Employee.objects.get(eid=pk)
        obj.delete()
        logger.info("Record is deleted")
        return redirect("show_url")
    
    
