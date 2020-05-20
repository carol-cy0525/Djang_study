from django.urls import path
from . import views

urlpatterns = [
    path('test/',views.ORMTest.as_view()),
]