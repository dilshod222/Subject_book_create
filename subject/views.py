
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from subject.models import Subject, Book, Course


class SubjectListView(TemplateView):
    template_name = 'subject_list.html'

    def get(self, request, *args, **kwargs):
        subjects = Subject.objects.filter(course_id=kwargs['pk']).all()
        course = Course.objects.get(pk=kwargs['pk'])



        return render(request, self.template_name, {'subjects': subjects,'course':course})


class BookListView(TemplateView):
    template_name = 'book_list.html'

    def get(self, request, *args, **kwargs):
        books = Book.objects.filter(subject_id=kwargs['pk']).all()

        return render(request, self.template_name, {'books': books})



class CreateCourseView(CreateView):

    def get(self, request, *args, **kwargs):
        self.template_name = 'create_course.html'
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        course = Course(name=name, created_by=request.user)
        course.save()

        return redirect('/')

class UpdateCourseView(UpdateView):
    def get(self, request, *args, **kwargs):
        course = Course.objects.get(pk=kwargs['pk'])
        self.template_name = 'update_course.html'
        return render(request, self.template_name,{'course':course})

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        course = Course.objects.get(pk=kwargs['pk'])
        course.name = name
        course.save()

        return redirect('/')

class DeleteCourseView(DeleteView):
    def get(self, request, *args, **kwargs):
        course = Course.objects.get(pk=kwargs['pk'])
        self.template_name = 'delete_course.html'
        return render(request, self.template_name,{'course':course})

    def post(self, request, *args, **kwargs):
        course = Course.objects.get(pk=kwargs['pk'])
        course.delete()

        return redirect('/')

class CreateSubjectView(CreateView):
    def get(self, request, *args, **kwargs):
        course = Course.objects.get(pk = kwargs['pk'])
        self.template_name = 'create_subject.html'
        return render(request, self.template_name, {'course':course})

    def post(self, request, *args, **kwargs):
        course = Course.objects.get(pk=kwargs['pk'])
        name = request.POST.get('name')
        subject = Subject(name=name, created_by=request.user, course_id=course.id)
        subject.save()

        return redirect('subject:subject_list', course.id)


class UpdateSubjectView(UpdateView):
    def get(self, request, *args, **kwargs):
        subject = Subject.objects.get(pk=kwargs['pk'])
        course = Course.objects.get(pk = subject.course_id)
        self.template_name = 'update_subject.html'
        return render(request, self.template_name,{'subject':subject, 'course':course})

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        subject = Subject.objects.get(pk=kwargs['pk'])
        subject.name = name
        subject.save()

        return redirect('subject:subject_list',subject.course_id)

class DeleteSubjectView(DeleteView):
    def get(self, request, *args, **kwargs):
        subject = Subject.objects.get(pk=kwargs['pk'])
        self.template_name = 'delete_subject.html'
        return render(request, self.template_name,{'subject':subject})

    def post(self, request, *args, **kwargs):
        subject = Subject.objects.get(pk=kwargs['pk'])
        _id = subject.course_id
        subject.delete()

        return redirect('subject:subject_list',_id)
