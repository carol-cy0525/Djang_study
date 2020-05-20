"""caroltest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include  #include包含的意思

# 注册自定义路由导包
from django.urls import register_converter
from converter import MobileConverter
# 注册自定义路由 参数一自定义路由文件名 参数路由二别名
register_converter(MobileConverter,"mobile")

# 工程总路由
urlpatterns = [
    path('admin/', admin.site.urls),

    # 将users子应用里的路由加到总路由
    # path('',include('子应用.urls')),
    path('',include('users.urls')),
    path('',include(('request_response.urls', 'request_response'), namespace='request_response')),
    path('',include('mysqltest.urls')),
]
