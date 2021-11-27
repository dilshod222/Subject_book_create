
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from os.path import join as join_path
from os.path import exists as path_exists
from os.path import basename as file_basename
# Create your views here.
from django.views.decorators.http import require_safe
from django.views.generic import (
    TemplateView, CreateView, UpdateView, DeleteView,
)

from subject.models import Subject, Book, Course
from subject_book.settings import MEDIA_ROOT, LOGIN_REDIRECT_URL
from uploads_app.models import Uploads
from uploads_app.utils import write_file, uploads_url


class SubjectListView(TemplateView):

    template_name = 'subject_list.html'

    def get(self, request, *args, **kwargs):
        subjects = Subject.objects.filter(course_id=kwargs['pk']).all()
        course = Course.objects.get(pk=kwargs['pk'])

        return render(request, self.template_name, {'subjects': subjects, 'course': course})


class BookListView(TemplateView):

    template_name = 'book_list.html'

    def get(self, request, *args, **kwargs):
        books = Book.objects.filter(subject_id=kwargs['pk']).all()
        subject = Subject.objects.get(pk=kwargs['pk'])
        return render(request, self.template_name, {'books': books, 'subject': subject})


class CreateCourseView(LoginRequiredMixin,CreateView):
    login_url = 'auth/login/'
    redirect_field_name = "login"
    permission_required = 'course.add_course'

    def get(self, request, *args, **kwargs):
        self.template_name = 'create_course.html'
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        course = Course(name=name, created_by=request.user)
        course.save()

        return redirect('/')


class UpdateCourseView(LoginRequiredMixin,UpdateView):
    login_url = LOGIN_REDIRECT_URL
    permission_required = ['course.add_course']


    def get(self, request, *args, **kwargs):
        course = Course.objects.get(pk=kwargs['pk'])
        self.template_name = 'update_course.html'
        return render(request, self.template_name, {'course': course})

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        course = Course.objects.get(pk=kwargs['pk'])
        course.name = name
        course.save()

        return redirect('/')


class DeleteCourseView(LoginRequiredMixin,DeleteView):
    login_url = LOGIN_REDIRECT_URL
    permission_required = ['course.add_course']
    def get(self, request, *args, **kwargs):
        course = Course.objects.get(pk=kwargs['pk'])
        self.template_name = 'delete_course.html'
        return render(request, self.template_name, {'course': course})

    def post(self, request, *args, **kwargs):
        course = Course.objects.get(pk=kwargs['pk'])
        course.delete()

        return redirect('/')


class CreateSubjectView(LoginRequiredMixin,CreateView):
    login_url = LOGIN_REDIRECT_URL
    permission_required = ['subject.add_subject']
    def get(self, request, *args, **kwargs):
        course = Course.objects.get(pk=kwargs['pk'])
        self.template_name = 'create_subject.html'
        return render(request, self.template_name, {'course': course})

    def post(self, request, *args, **kwargs):
        course = Course.objects.get(pk=kwargs['pk'])
        name = request.POST.get('name')
        subject = Subject(name=name, created_by=request.user, course_id=course.id)
        subject.save()

        return redirect('subject:subject_list', course.id)


class UpdateSubjectView(LoginRequiredMixin,UpdateView):
    login_url = LOGIN_REDIRECT_URL
    permission_required = ['subject.add_subject']
    def get(self, request, *args, **kwargs):
        subject = Subject.objects.get(pk=kwargs['pk'])
        course = Course.objects.get(pk=subject.course_id)
        self.template_name = 'update_subject.html'
        return render(request, self.template_name, {'subject': subject, 'course': course})

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        subject = Subject.objects.get(pk=kwargs['pk'])
        subject.name = name
        subject.save()

        return redirect('subject:subject_list', subject.course_id)


class DeleteSubjectView(LoginRequiredMixin,DeleteView):
    login_url = LOGIN_REDIRECT_URL
    permission_required = ['subject.add_subject']
    def get(self, request, *args, **kwargs):
        subject = Subject.objects.get(pk=kwargs['pk'])
        self.template_name = 'delete_subject.html'
        return render(request, self.template_name, {'subject': subject})

    def post(self, request, *args, **kwargs):
        subject = Subject.objects.get(pk=kwargs['pk'])
        _id = subject.course_id
        subject.delete()

        return redirect('subject:subject_list', _id)


class CreateBookView(LoginRequiredMixin,CreateView):
    login_url = LOGIN_REDIRECT_URL
    permission_required = ['book.add_book']
    def get(self, request, *args, **kwargs):
        subject = Subject.objects.get(pk=kwargs['pk'])
        self.template_name = 'create_book.html'
        return render(request, self.template_name, {'subject': subject})

    def post(self, request, *args, **kwargs):
        subject = Subject.objects.get(pk=kwargs['pk'])
        name = request.POST.get('name')
        author_name = request.POST.get('author_name')
        file = request.FILES['file']
        write_file(file)
        book = Book(name=name, created_by=request.user,
                    subject_id=subject.id,
                    author=author_name,
                    file=file, generated_name=uploads_url(file.name))
        book.save()

        return redirect('subject:book_list', subject.id)


class UpdateBookView(LoginRequiredMixin,UpdateView):
    login_url = LOGIN_REDIRECT_URL
    permission_required = ['book.add_book']
    def get(self, request, *args, **kwargs):
        book = Book.objects.get(pk=kwargs['pk'])
        subject = Subject.objects.get(pk=book.subject_id)
        self.template_name = 'update_book.html'
        return render(request, self.template_name, {'book': book, 'subject': subject})

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        author_name = request.POST.get('author_name')
        book = Book.objects.get(pk=kwargs['pk'])

        book.name = name
        book.author = author_name

        book.save()

        return redirect('subject:book_list', book.subject_id)


class DeleteBookView(LoginRequiredMixin,DeleteView):
    login_url = LOGIN_REDIRECT_URL
    permission_required = ['book.add_book']
    def get(self, request, *args, **kwargs):
        book = Book.objects.get(pk=kwargs['pk'])
        self.template_name = 'delete_book.html'
        return render(request, self.template_name, {'book': book})

    def post(self, request, *args, **kwargs):
        book = Book.objects.get(pk=kwargs['pk'])
        _id = book.subject_id
        book.delete()

        return redirect('subject:book_list', _id)

@require_safe
def download(request, generated_name):
    file = Uploads.objects.filter(generated_name=generated_name).first()
    path = join_path(MEDIA_ROOT, 'upload', file.generated_name)
    if path_exists(path):
        with open(path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type=file.content_type)
            response['Content-Disposition'] = 'inline; filename=' + file_basename(path)
        return response
    raise Http404
