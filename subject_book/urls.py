
from django.contrib import admin
from django.urls import path, include

from subject_book.home import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('course/', include('subject.urls')),
    path('auth/', include('authorization.urls')),
]
