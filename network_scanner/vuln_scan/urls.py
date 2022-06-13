from django.urls import path, include
from . import views

urlpatterns = [
 
    path('',views.vuln_home,name="vhome"),
    path('scan',views.vuln_scan,name="vscan")


]