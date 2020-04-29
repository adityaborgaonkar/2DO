from django.contrib import admin
from django.urls import path
from todo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todoView),
    path('addTodo/', addTodo),
    path('addBook/', addBook),
    path('addMusic/', addMusic),
    path('addCourse/', addCourse),
    path('addBinge/', addBinge),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
    path('deleteBook/<int:book_id>/', deleteBook),
    path('deleteMusic/<int:music_id>/', deleteMusic),
    path('deleteCourse/<int:course_id>/', deleteCourse),
    path('deleteBinge/<int:binge_id>/', deleteBinge),
]
