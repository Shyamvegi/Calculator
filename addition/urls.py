from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index'),
               path('calculate/<int:number1>/<int:number2>/',
                    views.getNumbers, name='getNumbers'),
               path('get_answer/<int:identifier>/',
                    views.getAnswer, name='getAnswer'),
               ]
