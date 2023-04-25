from django.urls import path
from .views import todo_list, delete_item

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('delete/<int:item_id>/', delete_item, name='delete_item'),
]
