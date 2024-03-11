from django.test import TestCase
from django.urls import reverse

from todo_list.models import Task


TASK_LIST_URL = reverse("todo_list:index")
SWITCH_TASK_STATUS_URL = reverse("todo_list:switch-task-status", kwargs={"pk": 1})


class TestViews(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            content="Test",
            status=False,
        )

    def test_switch_task_status(self):
        res = self.client.get(SWITCH_TASK_STATUS_URL)
        self.task.refresh_from_db()

        self.assertEqual(res.status_code, 302)
        self.assertTrue(self.task.status)

    def test_task_retrieve(self):
        res = self.client.get(TASK_LIST_URL)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["task_list"]),
            list(Task.objects.all())
        )
        self.assertTemplateUsed(res, "todo_list/index.html")
