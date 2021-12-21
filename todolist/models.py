from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE

# نموذج للتعامل مع المستخدمين
class User(AbstractUser):
    pass

# نموذج للتعامل مع القوائم
class listitems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.TextField()

    def __str__(self):
        return self.user and self.item

    # اضافة اختبار للنموذج
    def is_valid_listitems(self):
        return self.item != self.user and self.item > 1