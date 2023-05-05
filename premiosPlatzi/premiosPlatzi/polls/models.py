import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    #id django automáticamente hace un id prymary key
    question_text = models.CharField (max_length=200) #este modelo equivale a un varchar
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #si se bora una se van a borrar en cascada las respuestas
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text