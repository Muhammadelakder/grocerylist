from django.urls import include, path

from . import views

urlpatterns = [ 
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"), 
    path("list", views.list, name="list"),
    path("logout", views.logout_view, name="logout"),
    path("remove/<int:item_list>", views.remove, name="remove")
]