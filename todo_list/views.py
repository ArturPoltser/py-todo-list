from django.views import generic

from todo_list.models import Task


class IndexView(generic.ListView):
    model = Task
    template_name = "todo_list/index.html"
