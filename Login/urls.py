from . import views
from django.urls import path

urlpatterns = [
    path('Homepage/', views.Homepage),
]