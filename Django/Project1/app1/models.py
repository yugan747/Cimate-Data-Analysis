from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=20)
    grade = models.PositiveBigIntegerField()
    age = models.PositiveBigIntegerField()
    
    def __str__(self):
        return self.name 

