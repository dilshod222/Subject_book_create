from django.shortcuts import render

from subject.models import Course


def home(request):
    courses = Course.objects.all()
    return render(request,'home.html',{'courses':courses})