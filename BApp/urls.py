from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='Lists'),
    path('details/', views.details, name='Details')
]
