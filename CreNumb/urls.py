from django.urls import path

from CreNumb import views

urlpatterns = [
    path('',views.index, name='index'),
    path('year/<str:year>/',views.filterByYear,name='filter-by-year'),
    path('department/<str:department>/', views.filterByDepartment, name='filter-by-department'),
    path('logout/', views.logoutView, name='logout'),
    path('login/', views.loginView, name='login'),
    path('register/',views.registerView,name='register')
]