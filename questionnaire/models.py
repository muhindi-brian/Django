from django.db import models
from django.utils import timezone

gender_choices = [
    ('Male', "Male"),
    ('Female', "Female")
]

question_choices = [
    ('Yes', "Yes"),
    ('No', "No")
]

class QuestionnaireResponse(models.Model):
    
    gender = models.CharField(max_length=10,choices=gender_choices,default="Male")
    age = models.IntegerField()
    nationality = models.CharField(max_length=50)

    question_1 = models.CharField("Has your trip exceeded your expectations",max_length=5,choices=question_choices,default="Yes")
    

    date_published = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return("Questionnaire response "+str(self.pk))



# Create your models here.