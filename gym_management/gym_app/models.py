from django.db import models

# Create your models here.

class Gender(models.TextChoices):
    MALE = "Male"
    FUMALE = "Female"

class Sport(models.TextChoices):
    BOXING = "Boxing"
    KICKBOXING = "Kickboxing"
    MMA = "MMA"
    FITNESS = "Fitness"

class Member(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=50, choices=Gender.choices, null=False)
    number_phone = models.IntegerField(default=0, unique=True)
    category_sport = models.CharField(max_length=50, choices=Sport.choices, null=False)
    start_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['-start_at']

class Coach(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    phone = models.IntegerField(default=0,unique=True)
    coach_of = models.CharField(max_length=50, choices=Sport.choices, blank=False)
    start_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
  
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}" 