from django.urls import path
from . import views

# inv_management/           endpoints

urlpatterns = [
    path('hello/', views.say_hello)
]
