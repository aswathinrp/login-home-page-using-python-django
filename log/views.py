#from django.contrib.auth.decorators import login_required

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from . models import product
from django.contrib import messages
# Create your views here.
#@login_required()
def login_user(request):   
      
    if 'username' in request.session:
       return redirect(home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            request.session['username']=username
            return redirect(home)
        else:
            messages.error(request,'invalid entry !')
            return redirect(login_user)
    else:        
        return render(request,'login.html')
    

def home(request):
    if 'username' in request.session:
        products=product.objects.all()
        return render(request,'home.html',{'products':products})
    return redirect(login_user)
 

def logout_user(request):
      if 'username' in request.session:
          request.session.flush()   # clear
      return redirect(login_user)
