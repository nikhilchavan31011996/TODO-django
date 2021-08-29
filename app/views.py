from app.forms import TODOform
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app.forms import TODOform
from app.models import TODO
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    form = TODOform() #------here fields will be access from forms.py
    if request.user.is_authenticated: #here we can check user is loged or not....
        user = request.user
        # todos = TODO.objects.all() #----here we will get all objects from models.py
        todos = TODO.objects.filter(user=user).order_by('priority')
        res = render(request,'index.html',{'form':form, 'todos':todos})
        return res

def add_todo(request):
    if request.user.is_authenticated: #here we can check user is loged or not....
        user = request.user
        print(user)
        form = TODOform(request.POST)
        if form.is_valid():
            print(form.cleaned_data) #if we want ckeck fields data on cmd....for ckhecking purpose
            todo = form.save(commit=False) #commit is used to save the changes from user #False means--bydefault form will be change & True means--bydefaault form
            todo.user = user
            todo.save() #here actual data will be save in todo form
            print(todo)
            return redirect('home')    
        else:
            return render(request,'index.html',{'form':form})

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        log = {'form':form}
        res = render(request, 'login.html',log)
        return res
    else:
        form = AuthenticationForm(data=request.POST) #frontend data will be get here(backend)
        if form.is_valid():
            username = form.cleaned_data.get('username')  
            password = form.cleaned_data.get('password')
            user = authenticate(username= username, password= password)
            if user is not None:
                loginUser(request, user) #when we click on login page(html page), if user data is valid, then it will allow to reach to --------------------------the home page.
                return redirect('home')
        else:
            log = {'form':form}
            res = render(request, 'login.html',log)
            return res

#-----How to create user account???------
def signup(request):
    if request.method == 'GET':
        form = UserCreationForm() #here django provide bydefault signup form
        reg = {'form':form}
        return render(request,'signup.html',reg)
    
    else:
        #if method is post in HTML file,whatever we are fill the 'signup form' that all data will saved in database
        form = UserCreationForm(request.POST)
        reg = {'form':form}

        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:#here data will be verified, if data is already exist then it will show the same page ,otherwies it will redirct to the login page.
                return redirect('home')

        else:
            return render(request,'signup.html',reg)

def signout(request):
    logout(request)
    return redirect("login")

def delete_todo(request, id):
    TODO.objects.get(pk = id).delete()
    return redirect('home')

def change_status(request, id, status):
    todo = TODO.objects.get(pk= id)
    todo.status = status
    todo.save()
    return redirect('home')











