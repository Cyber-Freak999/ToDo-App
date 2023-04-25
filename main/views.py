from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoForm

def todo_list(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()

    items = TodoItem.objects.all()
    context = {'items': items, 'form': form}
    return render(request, 'main/index.html', context)

def delete_item(request, item_id):
    item = TodoItem.objects.get(id=item_id)
    item.delete()
    return redirect('todo_list')
