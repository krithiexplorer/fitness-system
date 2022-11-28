from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.home,name = "home"),
    path('mindfullness/',views.mindfullness,name = "mindfullness"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('recipes/',views.recipes,name="recipes"),
    path('exercises/',views.exercises,name="exercises")
]