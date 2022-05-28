from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.tool_home,name="thome"),
    path('ip',views.myip,name="ip")
    




]