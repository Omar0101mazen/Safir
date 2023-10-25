from django.urls import path
from . import views

urlpatterns = [
    path('', views.update_link, name='update_link')
]