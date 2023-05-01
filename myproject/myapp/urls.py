from django.urls import path
from . import views

urlpatterns = [
    path('simple_page/', views.simple_page, name='simple_page'),
]
