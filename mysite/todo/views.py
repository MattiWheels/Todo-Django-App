from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Max
from .models import TodoItem
from datetime import datetime
from pytz import timezone
import pytz

# Render the todo.html template and in the same request, send a dictionary of
# all items in the db.
def todoView(request):

    list_count = TodoItem.objects.all().aggregate(Max('todolist'))['todolist__max']
    all_items = {}

    if list_count is None:
        all_items['list_0'] = []
    elif list_count > 0:
        for i in range(list_count):
            items = [x for x in TodoItem.objects.filter(todolist=i)]
            all_items[f'list_{i}'] = items
    else:
        all_items['list_0'] = [x for x in TodoItem.objects.filter(todolist=0)]

    context = {
        'all_items': all_items,
        'list_count': list_count,
    }

    return render(request, 'todo.html', context)

# Create new TodoItem object and save it to the db.
def addTodo(request): # addTodo(request, list_id) to be implemented
    new_item = TodoItem()
    new_item.content = request.POST['content']

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

#def addTodoList(request):
    