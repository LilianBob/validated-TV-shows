from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import re, bcrypt

# Create your views here.



# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#     if not EMAIL_REGEX.match('email'):
#         return 
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.registration_val(request.POST)
        if len(errors) > 0:
            for key, val in errors.items():
                messages.error(request, val)
        return redirect("/")
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    hash_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hash_pw)
    return redirect('/')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if not User.objects.authenticate(email, password):
            messages.error(request, 'Email and Password do not match')
            return redirect("/")
        user = User.objects.get(email=email)
        request.session['user_id'] = user.id
        return redirect("/protected")
        return redirect('/')

def protected(request):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        context = {
        "user": user
        }
        return render(request, 'protected.html', context)
    else: 
        messages.error(request, 'You must be logged in to do that')
    return redirect("/")

def logout(request):
    del request.session['user_id']
    return redirect('/')