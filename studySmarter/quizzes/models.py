from django.db import models

class Questions(models.Model):
    
    class QuestionTypes(models.TextChoices):
            MCQ = "MCQ", "Mltiple Choice"
            SA = "SA", "Short Answer"
            TF = "TF", "True/False"   


    text = models.TextField()

    question_type = models.CharField(max_length=3, choices=QuestionTypes.choices)

    option1 = models.CharField(max_length=100, blank=True, null=True)
    option2 = models.CharField(max_length=100, blank=True, null=True)
    option3 = models.CharField(max_length=100, blank=True, null=True)
    option4 = models.CharField(max_length=100, blank=True, null=True)

    correct_answer = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.text