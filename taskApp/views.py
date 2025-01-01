from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate,login as LoginUser,logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from . forms import TaskForm,CustomUserCreationForm, ChangePasswordForm
from . models import Task
from django.utils import timezone
# Create your views here.

@login_required(login_url='loginpage')  
def addtask(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        task_description = request.POST.get('task_description')  
        task_deadline = request.POST.get('task_deadline')  
        task_assigned = request.POST.get('task_assigned')  
        task_status = request.POST.get('task_status')
        if request.user.is_authenticated:
            if not task_name:
                return render(request, 'index.html', {'error': 'Task name is required'})
            user = request.user
            if task_deadline:
                try:
                    deadline = timezone.datetime.strptime(task_deadline, '%Y-%m-%dT%H:%M')
                except ValueError:
                    return render(request, 'index.html', {'error': 'Invalid deadline format'})
            else:
                deadline = None
            assigned_user = User.objects.get(id=task_assigned)
            task = Task.objects.create(
                name=task_name,  
                description=task_description, 
                user=assigned_user,  
                status=task_status,  
                deadline=deadline,  
                addedby=user  
            )
            return redirect('tasklist')  
        else:
            return redirect('login')  
    else:
        users = User.objects.all()  
        return render(request, 'index.html', {'users': users})  
    
    
@login_required(login_url='loginpage')
def task_list(request):
    if request.user.is_staff:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(user=request.user)
    return render(request, 'home.html', {'tasks': tasks})


@login_required(login_url='loginpage')
def deletetask(request,id):
    if request.method=="POST":
        data = Task.objects.get(pk=id)
        data.delete()
        return redirect('tasklist')


@login_required(login_url='loginpage')
def updatetask(request, id):
    task = get_object_or_404(Task, pk=id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  
            return redirect('tasklist') 
        else:
            messages.error(request, "There was an error updating the task.") 
    else:
        form = TaskForm(instance=task)  
    return render(request, 'update.html', {'form': form, 'task': task})


@login_required(login_url='loginpage')
def search_tasks(request):
    query = request.GET.get('search_task')  
    tasks = Task.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query)
    ) if query else []  # Case-insensitive search in name or description
    return render(request, 'searchresult.html', {'tasks': tasks, 'query': query})


@login_required(login_url='loginpage')
def task_detail(request, id):
    task = get_object_or_404(Task, id=id)  # Fetch the task by ID or return a 404 error
    return render(request, 'task_detail.html', {'task': task})


def register(request):
    if request.method == "GET":
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('loginpage')
        else:
            return render(request, 'register.html', {'form': form})


def loginpage(request):
    if request.method=="GET":
        form=AuthenticationForm()
        return render(request, 'login.html',{'form':form})
    else:
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                LoginUser(request,user)
                return redirect('tasklist')
        else:
            return render(request,'login.html',{'form':form})


def logoutpage(request):
    logout(request)
    return redirect('loginpage')

@login_required(login_url='loginpage')
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  
            messages.success(request, 'Your password has been changed successfully!')
            return redirect('tasklist') 
        else:
            messages.error(request, 'There was an error with your password change.')
    else:
        form = ChangePasswordForm(user=request.user)
    
    return render(request, 'change_password.html', {'form': form})


def aboutus(request):
    return render(request, 'aboutus.html')