from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from wc_app3.models import User
def get_user(request):
    username="Sunck"
    userpassword="120"

    users=User.objects.filter(u_name=username)
    if users.count():
        user=users.first()
        if user.u_password==userpassword:
            result="获取用户信息成功"
        else:
            result="用户密码错误"
    else:
        result="用户不存在"

    return HttpResponse(result)