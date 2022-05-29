from email import message
from unittest import result
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import nmap
import socket
# Create your views here.
@login_required
def home(request):
    return render(request,"index.html")
def scan(request):
    if request.method == 'POST':
        target = request.POST['target']
        port = request.POST['port']
        
        sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((target,int(port)))
        if result == 0:
             message = "Port {}: \t Open".format(port)
             print("Port {}: \t Open".format(port))
        else:
            message = "Port {}: \t Closed".format(port)
            print("Port {}: \t Open".format(port))
            sock.close()
        d = { 'message' : message }
        return render(request,"result.html",d)
    return render(request,"scan.html")

def basic_scan(request):
    res = [
                    {'port':21,'state':'Closed','service':'SSH'},
                    {'port':22,'state':'Closed','service':'FTP'},
                    {'port':80,'state':'Closed','service':'HTTP'},
                    {'port':8000,'state':'Closed','service':'HTTPS'},
                    {'port':3000,'state':'Closed','service':'Telnet'}

                ]
    if request.method == 'POST':
        target = request.POST['target']
        portlist = [21,22,80,443,3000,8000,8080]
                
        for i in range(0,len(res)):
                sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                sock.settimeout(5)
                result = sock.connect_ex((target,res[i]['port']))
                if result == 0:
                    res[i]['state'] = "Open"
                else:
                    sock.close()
               
        return render(request,"result.html",{'res':res})
    return render(request,"basic_scan.html")

def custom_scan(request):
    if request.method == 'POST':
        target = request.POST['target']
        ports = request.POST['port']

        nm = nmap.PortScanner()
        res = nm.scan(target,ports)

        return render(request,'result.html',{'res':res})
    return render(request,'custom_scan.html')
def advanced_scan(request):
    return render(request,'advanced_scan.html')
def ping_scan(request):
    return render(request,'ping_scan.html')
def tcp_scan(request):
    return render(request,"tcp_scan.html")
def udp_scan(request):
    return render(request,"udp_scan.html")
def stealth_scan(request):
    return render(request,"stealth_scan.html")
def aggressive_scan(request):
    return render(request,"aggressive_scan.html")
def full_scan(request):
    return render(request,"full_scan.html")

def my_scan(request):
    return render(request,'my_scan.html')