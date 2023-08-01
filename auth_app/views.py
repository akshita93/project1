from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django .shortcuts import render,redirect


class Sign_up(View):
    def get(self,request):
        template_name='auth_app/signup.html'
        form=UserCreationForm()
        context={'form':form}
        return render(request,template_name,context)
    
    def post(self,request):
        template_name='auth_app/signup.html'
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin_url')
        context={'form':form}
        return render(request,template_name,context)
    

class Login_view(View):
    def get(self,request):
        template_name = 'auth_app/login.html'
        context={}
        return render(request, template_name, context)
    
    def post(self,request):
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        user = authenticate(username=un, password=pw)
        if user:
            login(request, user)
            return redirect('show_url')
        template_name = 'auth_app/login.html'
        context = {}
        return render(request, template_name, context) 

class Logout_view(View):
    def get(self,request):
        logout(request)
        return redirect('signin_url')   


