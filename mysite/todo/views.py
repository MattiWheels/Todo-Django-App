from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
from datetime import datetime
from pytz import timezone
import pytz

# Render the todo.html template and in the same request, send a dictionary of
# all items in the db.
def todoView(request):

    all_items = TodoItem.objects.all()

    # Comment out whichever template you don't want to render.
    #return render(request, 'testing.html',
    return render(request, 'todo.html',
        {
            'all_items': all_items,
        }
    )

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
