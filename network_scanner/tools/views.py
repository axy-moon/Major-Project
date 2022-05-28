from ipaddress import ip_address
from django.shortcuts import render
import socket
from requests import get

# Create your views here.

def tool_home(request):
    return render(request,'tool_index.html')

def myip(request):
      
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname)   
    public_ip = get('https://api.ipify.org').text
    
    ip = {'ipv4':IPAddr,'public_ip':public_ip}

    return render(request,'ip.html',ip)