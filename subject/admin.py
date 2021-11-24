from django.contrib import admin

# Register your models here.
from subject.models import Employee, Book, Subject, Course

admin.site.register(Employee)
admin.site.register(Course)
admin.site.register(Book)
admin.site.register(Subject)
