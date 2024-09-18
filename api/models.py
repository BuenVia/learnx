from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=90)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "subjects"

    def __str__(self) -> str:
        return f"Subject: {self.name}"

class Category(models.Model):
    name = models.CharField(max_length=90)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "categorys"

    def __str__(self) -> str:
        return f"Category: {self.name}"

# Learn
class Learn(models.Model):
    name = models.CharField(max_length=90)
    author = models.CharField(max_length=90)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "learns"

    def __str__(self) -> str:
        return f"Learn: {self.name}"

# Practice
class PracticeSection(models.Model):
    instruction = models.TextField(blank=True)
    learn = models.ForeignKey(Learn, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "practice_sections"

    def __str__(self) -> str:
        return f"Practice Section: {self.name}"

class Questions(models.Model):
    test_type = models.IntegerField()
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    option_one = models.CharField(max_length=255, blank=True)
    option_two = models.CharField(max_length=255, blank=True)
    option_three = models.CharField(max_length=255, blank=True)
    feedback = models.CharField(max_length=255, blank=True)
    practice_section = models.ForeignKey(PracticeSection, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "questions"

    def __str__(self) -> str:
        return f"Practice Question: {self.question}" 

# Test
class TestData(models.Model):
    date_taken = models.DateTimeField(auto_now_add=False)
    learn = models.ForeignKey(Learn, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "test_datas"

    def __str__(self) -> str:
        return f"Test Data: {self.question}" 