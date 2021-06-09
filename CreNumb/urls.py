from django.urls import path

from CreNumb import views

urlpatterns = [
    path('',views.index, name='index')
]