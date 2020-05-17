from django.urls import path
from . import views

urlpatterns = [
    path('querystring/',views.QSParamView.as_view()),
    path('formdata/', views.FormDataParamView.as_view()),

    path('url_param1/<int:num>/', views.URLParam1View.as_view()),
    path('url_param2/<mobile:phone_num>/', views.URLParam2View.as_view()),
]