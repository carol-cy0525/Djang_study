# 必须定义一个路由样式列表
# 名字必须是 urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    # path(网络地址正则表达式, 视图函数名),
    path("users/register",views.register),
]






