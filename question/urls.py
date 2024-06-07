from django.urls import path
from . import views

urlpatterns = [
    path('paper', views.paper,name='paper'),
    path('question', views.question_list,name='question_list'),
    path('question/upload', views.upload_question,name='upload_question'),
    path('question/<int:pk>/', views.delete_question, name='delete_question'),
]