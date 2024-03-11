from django.test import TestCase
from todo_list.models import Tag
from todo_list.forms import TaskForm


class TaskFormTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(
            pk=1,
            name="test"
        )
        self.form_data = {
            "content": "Complete task",
            "deadline": "2022-03-10T18:00:00Z",
            "tag": [1],
        }

    def test_valid_form(self):
        form = TaskForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        self.form_data["content"] = ""
        form = TaskForm(data=self.form_data)
        self.assertFalse(form.is_valid())
