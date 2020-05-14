from django.shortcuts import render
from django import http

# Create your views here.

# 以下代码用于定义函数视图的
def register(request):
    """
    用户注册函数视图
    :param request: 请求对象
    :return: 响应对象
    """
    return http.HttpResponse("这里是注册页面的响应体")







