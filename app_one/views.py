from django.shortcuts import render, redirect,HttpResponse
from . import models
from django.contrib import messages
from .models import User
import bcrypt
from .models import Pie

def index(request):
    return render(request,'index.html')


def dashboard(request):
    if  'userid' not in request.session:
        return redirect('/')
    else:
        context = {
                "logged_user" : models.get_specific_user(request)
            }
        return render(request,'welcome.html' , context)


def show(request,ic):
    context={
        'specific_pie':models.show_specific_pie(ic),
        "logged_user" : models.get_specific_user(request),
    }
    return render(request,'show.html',context)

def voting(request):
    models.vote_update_pie(request)
    return redirect('/pies')


def delete_pie(request,ip):
    models.delete_piee(ip)
    return redirect('/dashboard')

def display_all_pies(request):
    context={
        'all_pies':models.show_all_pies()
    }
    return render(request,'allpies.html',context)



def create_pie(request):
    errors = Pie.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/dashboard')
    else:
        models.create_a_book(request)
        return redirect('/dashboard')
    

def edit(request,num):
    context={
        'specific_pie':models.shows_pecificpie(num)
    }
    return render(request,'edit.html',context)

def edit_pie(request):
    errors = Pie.objects.book_validator(request.POST)
    if len(errors) > 0:
        x=request.POST['hidden_id']
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit/{x}')
    else:
        models.update_pie(request)
        return redirect('/dashboard')


def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        models.register(request)
        
        return redirect('/')




def login(request):
    user = User.objects.filter(email = request.POST['person_email'])
    if not user:
        return redirect('/')
    else :
        logged_user = user[0]
    
        if bcrypt.checkpw(request.POST['password_email'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/dashboard')
    return redirect('/')



def logout(request):
    del request.session['userid']
    return redirect('/')

