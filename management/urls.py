from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),  # Maps /menu/ to the menu view
]
