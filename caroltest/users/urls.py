# 必须定义一个路由样式列表
# 名字必须是 urlpatterns
from django.urls import path, re_path
from . import views

urlpatterns = [
    # path(网络地址正则表达式, 视图函数名),
    # path("users/register/",views.register),

    # 类视图路由写法
    path("users/register/",views.RegisterClassView.as_view()),

    # views.RegisterClassView.as_view()  调用as_view() 返回的是一个view   相当于这里写的是这个返回的view (视图函数名)

    # path('users/login/',views.Login.as_view()),
    # re_path写法
    re_path(r'^users/login/$',views.Login.as_view()),

]






