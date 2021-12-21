import unittest
from django.test import TestCase

from todolist.models import listitems, User

# Create your tests here.

# التحقق من اضافة العنصر الي قاعدة البيانات
class ListItemsTestcase(TestCase):

        # اعداد قاعدة بيانات جديده للاختبار
        def setUP(Self):
                user = User.objects.create_user(username, "username")
                a1 = listitems.objects.create(user=user, item="tada")

        def test_items(self):
                user = User.objects.get(username="username")
                l = listitems.objects.get(user=user, item="tada")
                self.assertTrue(l.is_valid_listitems())

        