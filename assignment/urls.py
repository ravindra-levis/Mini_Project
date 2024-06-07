from django.urls import path
from . import views

urlpatterns = [
    path('assignment', views.assignment_list,name='assignment_list'),
    path('assignment/upload', views.upload_assignment,name='upload_assignment'),
    path('assignment/<int:pk>/', views.delete_assignment, name='delete_assignment'),

]