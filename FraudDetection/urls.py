from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name = 'homepage'),
    path('result/', views.resultpredict, name = 'result'),
]


