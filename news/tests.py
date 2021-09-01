from django.test import TestCase
from .models import Editor,Article,tags

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Mark= Editor(first_name = 'mark', last_name ='Muiri', email ='markmuiri@moringaschool.com')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Mark,Editor))


# Testing Save Method
    def test_save_method(self):
        self.Mark.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)