from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Max
from .models import TodoItem
from datetime import datetime
from pytz import timezone
import pytz


# Render the todo.html template and send a dictionary of all items in the db.
# This is the default view located at '/'
def todoView(request):

    all_items = getLists()

    context = {
        'all_items': all_items,
    }

    return render(request, 'todo.html', context)

# Create a new list and render todo.html with context containing the new list
def addList(request, new_list_id):

    all_items = getLists()
    all_items[f'list_{new_list_id}'] = {}

    return render(request, 'todo.html', {'all_items': all_items})

# Gets all of the todolists and separates them by number (models.TodoItem.todolist)
def getLists():

    # Max_list is the highest numbered todolist attribute (integer)
    max_list = TodoItem.objects.all().aggregate(Max('todolist'))['todolist__max']
    all_items = {}

    # If no todolists or todolist items exist, create empty todolist / maintain default todolist
    if max_list is None:
        all_items['list_0'] = {}

    # If there are multiple todolists, pair them with their values in a dictionary
    elif max_list > 0:
        for i in range(max_list+1):
            all_items[f'list_{i}'] = TodoItem.objects.filter(todolist=i)

    # If only the default list exists with some todos, 
    else: 
        all_items['list_0'] = TodoItem.objects.filter(todolist=0)

    return all_items

# Create new TodoItem object and save it to the db.
def addTodo(request, list_id):
    new_item = TodoItem()
    new_item.content = request.POST['content']
    new_item.todolist = list_id

    # Generate timestamp for todo item.
    date_format = '%m/%d/%Y %H:%M:%S %Z'
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('US/Pacific'))
    new_item.time = date.strftime(date_format)

    # Save item to db and redirect to home page.
    new_item.save()
    return HttpResponseRedirect('/')

# Delete item by ID and redirect to todoView.
def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/')
