from django.test import TestCase

from todo_list.models import Tag, Task


class TestModels(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Personal")
        self.task = Task.objects.create(
            content="Test",
            status=False,
        )

    def test_tag_str(self):
        self.assertEqual(str(self.tag), "Personal")

    def test_task_str(self):
        self.assertEqual(str(self.task), "Test")
