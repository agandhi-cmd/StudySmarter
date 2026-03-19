from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'quizzes/dashboard.html')

def profile(request):
    return render(request, 'quizzes/profile.html')

def quiz(request):
    return render(request, 'quizzes/quiz.html')