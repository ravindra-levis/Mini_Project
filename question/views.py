from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import QuestionForm
from .models import Question
from django.contrib.auth.models import Group
from .decorators import teacher_only,allowed_users
# Create your views here.

def paper(request):
    return render(request,'works.html')

def question_list(request):
    questions=Question.objects.all()
    return render(request,'question_list.html',{
        'questions':questions
    })
# @teacher_only
@allowed_users(allowed_roles=['teacher'])
def upload_question(request):
    if request.method =="POST":
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('question_list')
    else:
        form = QuestionForm()
    return render(request, 'upload_question.html', {
        'form': form
    })
# @teacher_only
@allowed_users(allowed_roles=['teacher'])
def delete_question(request, pk):
    if request.method == 'POST':
        question = Question.objects.get(pk=pk)
        question.delete()
    return redirect('question_list')
