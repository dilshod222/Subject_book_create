from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    picture = models.FileField(upload_to='images/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'employee'
    def __str__(self):
        return self.user.username

class Course(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Course'



class Subject(models.Model):
    name = models.CharField(max_length=200, null=False)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table = 'Subject'
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=200, null=True)
    file = models.FileField(upload_to='upload/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Book'
    def __str__(self):
        return self.name