from django.db import models
from django.contrib.auth.models import User

PROGRES=[
   ( "high","high"),
   ( "good","good"),
    ("medium","medium"),
    ("weak","weak"),
]
class Student(models.Model):
    faname=models.CharField(max_length=50)
    phoneno=models.BigIntegerField()
    classno=models.IntegerField()
    cteacher=models.CharField(max_length=100)
    user_model = models.ForeignKey(User, on_delete=models.CASCADE)

    def __int__(self):
        return self.classno
    
    class Meta:
        verbose_name_plural = "Student"

