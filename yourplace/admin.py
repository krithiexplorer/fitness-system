from django.contrib import admin
from .models import Yoga
from .models import Exercises
from .models import Recipes

# Register your models here.
admin.site.register(Yoga)
admin.site.register(Exercises)
admin.site.register(Recipes)
