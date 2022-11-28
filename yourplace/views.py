from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'your_place.html')

def mindfullness(request):
    return render(request,'yourplace_mindfullness.html')    

def login(request):
    return render(request,'yourplace_login.html')

def signup(request):
    return render(request,'yourplace_signup.html')

def recipes(request):
    return render(request,'yourplace_recipes.html')

def exercises(request):
    return render(request,'yourplace_exercises.html')