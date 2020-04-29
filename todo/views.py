from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
import datetime

today_date = datetime.datetime.now()
today_date = today_date.strftime("%A, %B %d, %Y.")

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    all_book_items = BookItem.objects.all()
    all_music_items = MusicItem.objects.all()
    all_course_items = CourseItem.objects.all() 
    all_binge_items = BingeItem.objects.all()

    # Parsing all items via JSON object
    data = {
        'today_date':today_date,
		'all_todo_items': all_todo_items,
        'all_book_items': all_book_items,
        'all_music_items': all_music_items,
        'all_course_items': all_course_items,
        'all_binge_items': all_binge_items,
		}
    return render(request, 'todo.html', data)

# ADD ITEM

def addTodo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/')

def addBook(request):
    new_book = BookItem(content = request.POST['content'])
    new_book.save()
    return HttpResponseRedirect('/')

def addMusic(request):
    new_music = MusicItem(content = request.POST['content'])
    new_music.save()
    return HttpResponseRedirect('/')

def addCourse(request):
    new_course = CourseItem(content = request.POST['content'])
    new_course.save()
    return HttpResponseRedirect('/')

def addBinge(request):
    new_binge = BingeItem(content = request.POST['content'])
    new_binge.save()
    return HttpResponseRedirect('/')

# DELETE ITEM

def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/')
     
def deleteBook(request, book_id):
    book_to_delete = BookItem.objects.get(id=book_id)
    book_to_delete.delete()
    return HttpResponseRedirect('/')

def deleteMusic(request, music_id):
    music_to_delete = MusicItem.objects.get(id=music_id)
    music_to_delete.delete()
    return HttpResponseRedirect('/')

def deleteCourse(request, course_id):
    course_to_delete = CourseItem.objects.get(id=course_id)
    course_to_delete.delete()
    return HttpResponseRedirect('/')
    
def deleteBinge(request, binge_id):
    binge_to_delete = BingeItem.objects.get(id=binge_id)
    binge_to_delete.delete()
    return HttpResponseRedirect('/')