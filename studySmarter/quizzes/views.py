from django.shortcuts import render
from django.http import HttpResponse
from .models import Questions

def home(request):
    return render(request, 'quizzes/dashboard.html')

def profile(request):
    return render(request, 'quizzes/profile.html')

def quiz(request):
    return render(request, 'quizzes/quiz.html')


def quiz_views(request):
    questions = Questions.objects.all()
    score = 0 

    if request.method == "POST":
        for q in questions:
            user_answer = request.POST.get(f"q{q.id}")

            if user_answer and user_answer == q.correct_answer:
                score += 1 

        return render(request, "quizzes/result.html", {"score": score})
    return render(request, "quizzes/quiz.html", {"questions": questions})