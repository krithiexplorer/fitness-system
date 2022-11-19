from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.home,name = "home"),
    path('mindfullness/',views.mindfullness,name = "mindfullness")
]