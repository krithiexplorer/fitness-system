from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.home,name = "home"),
    path('mindfullness/',views.mindfullness,name = "mindfullness"),
    path('yourbmi/',views.yourbmi,name ="yourbmi"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('signup/',views.signup,name="signup"),
    path('recipes/',views.recipes,name="recipes"),
    path('exercises/',views.exercises,name="exercises")
]