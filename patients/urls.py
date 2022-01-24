
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.Patients.as_view()),
    # path('register/<int:pk>/', views.Patients.as_view()),

]