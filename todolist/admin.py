from django.contrib import admin
from .models import User, listitems

# Register your models here.
admin.site.register(User)

admin.site.register(listitems)