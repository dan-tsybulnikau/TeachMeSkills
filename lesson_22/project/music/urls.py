from django.urls import path,re_path, reverse
from . import views

urlpatterns = [
    path('', views.index, name='class_view'),
    path('contacts/', views.contacts, name='contacts'),
]




