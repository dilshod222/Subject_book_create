from django.urls import path

from subject.views import (
    SubjectListView,
    BookListView,
    CreateCourseView,
    UpdateCourseView,
    DeleteCourseView,
    CreateSubjectView,
    UpdateSubjectView,
    DeleteSubjectView,
    CreateBookView,
    UpdateBookView,
    DeleteBookView,
    download,

)

app_name = 'subject'

urlpatterns = [
    path('subject/<int:pk>', SubjectListView.as_view(), name='subject_list'),
    path('book_list/<int:pk>', BookListView.as_view(), name='book_list'),
    path('create_course/', CreateCourseView.as_view(), name='create_course'),
    path('update_course/<int:pk>', UpdateCourseView.as_view(), name='update_course'),
    path('delete_course/<int:pk>', DeleteCourseView.as_view(), name='delete_course'),
    path('create_subject/<int:pk>', CreateSubjectView.as_view(), name='create_subject'),
    path('update_subject/<int:pk>', UpdateSubjectView.as_view(), name='update_subject'),
    path('delete_subject/<int:pk>', DeleteSubjectView.as_view(), name='delete_subject'),
    path('create_book/<int:pk>', CreateBookView.as_view(), name='create_book'),
    path('update_book/<int:pk>', UpdateBookView.as_view(), name='update_book'),
    path('delete_book/<int:pk>', DeleteBookView.as_view(), name='delete_book'),
    path('download_book/<str:generated_name>', download, name='download_book'),
]
