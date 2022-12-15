from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Yoga
from .models import Exercises
from .models import Recipes
from django.contrib.auth.models import User, auth
from django.contrib import messages
from joblib import load

model = load('./savedmodels/rfc.joblib')

# Create your views here.
def home(request):
    return render(request,'your_place.html')

def logout(request):
    auth.logout(request)
    return redirect('/')   

def mindfullness(request):
    stretches = Yoga.objects.all()
    return render(request,'yourplace_mindfullness.html',{'stretches':stretches})  

def yourbmi(request):
    if request.method == 'POST':
        gender = request.POST['gender']   
        if gender == 'male':
            gender = 1
        else:
            gender = 0     
        height = request.POST['height']
        weight = request.POST['weight']
        y_pred = model.predict([[gender,height,weight]])
        if y_pred[0] == 'Extremely Underweight':
            y_pred = 'You are extremely underweight!!, consider some of the most healthy shakes and foods available out there!! check out our recipes and yogas section to healthily gain weight.'
        elif y_pred[0] == 'Underweight':
            y_pred = 'You are underweight!!, consider some of the most healthy shakes and foods available out there!! check out our recipes and yogas section to healthily gain weight.'
        elif y_pred[0] == 'Overweight':
            y_pred = 'You are overweight!!, consider some of the most healthy shakes and foods available out there!! check out our exercises and yogas section to reduce weight naturally.'    
        elif y_pred[0] == 'Normal':
            y_pred = 'You are under perfect weight! Congratulations!! Follow a healthy diet by having healthy foods, practicing these exercises and maintain good health!!'    
        elif y_pred[0] == 'Obese':
            y_pred = 'You are Obese! Dont worry!, consider some of the most healthy shakes and foods available out there!! check out our exercises and yogas section to reduce weight naturally.'
        else:
            y_pred = 'You are Extremely Obese! Take action Immediately!, consider some of the most healthy shakes and foods available out there!! check out our exercises and yogas section to reduce weight naturally.'
        return render(request,'yourplace_bmi.html',{'result':y_pred}) 
    else:    
        return render(request,'yourplace_bmi.html')      
   
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'* Invalid credentials,Try Again!!!')  
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:        
            return render(request,'yourplace_login.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'* Username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'* Email already in use')
                return redirect('signup')
            else:
                user = User.objects.create_user(username = username, password = password1, email = email,first_name = first_name, last_name = last_name)
                user.save()
                auth.login(request,user)
                return redirect('/')
        

        else:
            messages.info(request,'* Passwords dont match')
            return redirect('signup')  
                    

    else:    
        return render(request,'yourplace_signup.html')

def recipes(request):
    recipe = Recipes.objects.all()
    return render(request,'yourplace_recipes.html',{'recipe' : recipe})

def exercises(request):
    exercise = Exercises.objects.all()
    return render(request,'yourplace_exercises.html',{'exercise' : exercise})