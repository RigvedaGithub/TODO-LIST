from django.urls import path
from .import views
urlpatterns = [
    path("",views.todo_list),
    path("delete-task/<id>",views.delete_task),
    path("edit-task/<id>",views.edit_task),
    # path("update-task/<id>",views.update_task)
]
