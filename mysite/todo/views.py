from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

# Render the todo.html template and in the same request, send a dictionary of
# all items in the db.
def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
        {'all_items': all_todo_items})

# Save the request content sent via form input submit. Redirect to todoView.
def addTodo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

# Delete the item at the selected ID. Request via form input delete. Redirect to todoView.
def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
