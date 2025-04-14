from django.urls import path

from todo.views import (
    HomePageView,
    TagsListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskCompleteUndoView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

app_name = "todo"

urlpatterns = [
    # TASK URLS
    path("", HomePageView.as_view(), name="index"),
    path("t/create/", TaskCreateView.as_view(), name="task-create"),
    path("todo/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("todo/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("todo/<int:pk>/status/", TaskCompleteUndoView.as_view(), name="task-status"),
    # TAGS URLS
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>delete/", TagDeleteView.as_view(), name="tag-delete"),
]
