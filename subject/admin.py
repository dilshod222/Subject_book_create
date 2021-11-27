from django.contrib import admin

# Register your models here.
# from authorization.models import Employe
from subject.models import Book, Subject, Course

# admin.site.register(Employe)
admin.site.register(Course)
admin.site.register(Book)
admin.site.register(Subject)
