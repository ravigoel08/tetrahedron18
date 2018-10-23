from . import views
from django.urls import path

urlpatterns = [
    path('',views.Home,name="Home"),
    path('index/',views.index,name="index"),
    path('registered/',views.registered,name="registered"),
    path('exportmeout/',views.export,name="export"),
   # path('',views.Registered,name="registered")
]
