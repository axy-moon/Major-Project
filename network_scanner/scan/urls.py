from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    
    path('my_scans/',views.my_scan,name="my_scan"),

    path('basic_scan/',views.basic_scan,name="basic_scan"),
    path('advanced_scan/',views.advanced_scan,name="advanced_scan"),
    path('custom_scan/',views.custom_scan,name="custom_scan"),
    
    path('ping_scan/',views.ping_scan,name="ping_scan"),
    path('tcp_scan/',views.tcp_scan,name="tcp_scan"),
    path('udp_scan/',views.udp_scan,name="udp_scan"),

    path('stealth_scan/',views.stealth_scan,name="stealth_scan"),
    path('aggressive_scan/',views.aggressive_scan,name="aggressive_scan"),
    path('full_scan/',views.full_scan,name="full_scan")





]