from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from todo.forms import TaskCreationForm
from todo.models import Task, Tag


class HomePageView(generic.ListView):
    model = Task
    template_name = "todo/index.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = Task.objects.prefetch_related("tags")
        tag_id = self.request.GET.get("tag")
        status = self.request.GET.get("tag_status")

        if tag_id:
            queryset = queryset.filter(tags__id=tag_id)

        if status == "done":
            queryset = queryset.filter(is_done=True)
        elif status == "undone":
            queryset = queryset.filter(is_done=False)
        elif status == "today":
            queryset = queryset.filter(deadline__date__lte=timezone.now().date())

        return queryset.order_by("is_done", "-created_at")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreationForm

    def get_success_url(self):
        return reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreationForm

    def get_success_url(self):
        return reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task

    def get_success_url(self):
        return reverse_lazy("todo:index")


class TaskCompleteUndoView(generic.View):
    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)

        action_map = {
            "complete": True,
            "remove": False,
        }
        action = request.POST.get("action")
        if action in action_map:
            task.is_done = action_map[action]
            task.save()

        next_url = request.POST.get("next")
        return redirect(next_url or "todo:home")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]

    def get_success_url(self):
        return reverse_lazy("todo:tags-list")


class TagsListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]

    def get_success_url(self):
        return reverse_lazy("todo:tags-list")


class TagDeleteView(generic.DeleteView):
    model = Tag

    def get_success_url(self):
        return reverse_lazy("todo:tags-list")
