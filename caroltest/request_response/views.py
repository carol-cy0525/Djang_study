from django.shortcuts import render

# Create your views here.
from django.views import View
from django import http

class QSParamView(View):
    """测试提取查询字符串参数
        http://127.0.0.1:8000/querystring/?name=zxc&age=18
    """
    def get(self,request):
        # 获取查询字符串参数name age
        name = request.GET.get('name','小明')
        age = request.GET.get('age','18')
        return http.HttpResponse('查询字符串参数：%s %s' % (name,age))



class FormDataParamView(View):
    """测试提取表单类型请求体参数
    http://127.0.0.1:8000/formdata/
    """

    def post(self, request):
        # 获取表单类型请求体参数中的username、password
        username = request.POST.get('username')
        password = request.POST.get('password')

        return http.HttpResponse('表单类型请求体参数：%s--%s' % (username, password))


