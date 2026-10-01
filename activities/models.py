from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    user=models.ForeignKey(User, on_delete= models.CASCADE)
    category=models.CharField(max_length=50)
    def __str__(self):
        return self.category

class Activity(models.Model):
    FREQ_UNIT=[
        ('Days','Days'),
        ('Weeks','Weeks'),
        ('Months','Months'),
        ('Years','Years')
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    frequency=models.PositiveIntegerField()
    frequency_unit=models.CharField(max_length=10, choices=FREQ_UNIT)
    planned_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class CompletionHistory(models.Model):
    activity=models.ForeignKey(Activity, on_delete=models.CASCADE)
    completed_at=models.DateField()
    def __str__(self):
       return f"{self.activity.name} - {self.completed_at}"