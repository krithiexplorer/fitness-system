from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'your_place.html')

def mindfullness(request):
    return render(request,'yourplace_mindfullness.html')    