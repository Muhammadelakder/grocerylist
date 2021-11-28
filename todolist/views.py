from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from .models import User, listitems

def index(request):

    # اذا كان المتسخدم قد سجل الدخول
    if request.user.is_authenticated:

        return HttpResponseRedirect(reverse("list"))

    # غير ذلك اعرض علي المستخدم التسجيل
    else:
        return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]

        # تأكد من تطابق كلمة السر
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "todolist/register.html", {
                "message": "كلمة السر غير متطابقه"
            })

        # البدء بإنشاء مستخدم جديد
        try:
            user = User.objects.create_user(username, username, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "todolist/register.html", {
                "message": "اسم المستخدم موجود"
            })

        
        login(request, user)
        return HttpResponseRedirect(reverse("list"))

    
    else:
        return render(request, "todolist/register.html")


def login_view(request):
    if request.method == "POST":

        # البدء بتسجيل الدخول
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("list"))

        else: 
            return render(request, "todolist/login.html", {
                "message" : "اسم المستخدم / أو كلمة المرور غير صحيحة"
            })

    else:
        return render(request, "todolist/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


@login_required
def list(request):
    user = request.user

    # اظهار القائمه الحاليه
    items = listitems.objects.all().filter(user=user)

    if request.method == 'POST':

        # اضافة عنصر للقائمه
        item = request.POST["item"]
        add = listitems.objects.create(user=user, item=item)
        add.save()

    return render(request, "todolist/list.html", {
        "items": items
    })


@login_required
def remove(request, item_list):
    if request.method == 'POST':

        # مسح عنصر من القائمه
        f = listitems.objects.all().get(id=item_list)
        f.delete()

        return HttpResponseRedirect(reverse("list"))