from django.urls import path

from employees import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('employees/', views.employees, name="employees"),
    path('add_employee/', views.add_employee, name="add_employee"),
    path('suit/', views.suit, name="suit"),
    path('add_suit/', views.add_suit, name="add_suit"),
    path('allocate_suit/', views.allocate_suit, name="allocate_suit"),
    path('realtime_data/', views.realtime_data, name="realtime_data"),
    path('delete_suit/', views.delete_suit, name="delete_suit"),
    path('delete_employee/', views.delete_employee, name="delete_employee"),
    path('<id>/update_employee', views.update_employee, name="update_employee"),
    path('<id>/update_suit', views.update_suit, name="update_suit"),
]
