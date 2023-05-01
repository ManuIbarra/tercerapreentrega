from django.urls import path
from . import views

urlpatterns = [
    # Map the root URL to the hello_world view
    path('', views.hello_world, name='hello_world'),
]
