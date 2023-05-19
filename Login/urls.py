from . import views
from django.urls import path

urlpatterns = [
    path('Homepage/', views.Homepage),
    path('Alldata/<int:pk>', views.Alldata),
    #path('Update/',views.Update),
    path('get/',views.get),
]