from django.urls import path
from . import views

urlpatterns = [
    path('querystring/',views.QSParamView.as_view()),
    path('formdata/', views.FormDataParamView.as_view()),
]