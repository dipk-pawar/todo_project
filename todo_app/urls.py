from .views import *
from django.urls import path

urlpatterns = [
    path("create-todo/", create_todo, name="create_todo"),
    path("compeleted_task/<int:id>", complete_task, name="complete_task"),
    path("uncompeleted_task/<int:id>", un_complete_task, name="uncomplete_task"),
    path("update_task/<int:id>", edit_post, name="edit_task"),
    path("delete_task/<int:id>", delete_task, name="delete_task"),
]
