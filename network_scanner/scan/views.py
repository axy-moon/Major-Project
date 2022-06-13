from email import message
from unittest import result
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import nmap
import socket
# Create your views here.

scanner = nmap.PortScanner()

@login_required
def home(request):
    return render(request,"index.html")

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
    return render(request,"result.html")

def custom_scan(request):
   
    if request.method == 'POST':
        target = request.POST['target']
        ports = request.POST['port']

        scanner = nmap.PortScanner()
        res = scanner.scan(target,ports)
        
        if res['nmap']['scanstats']['uphosts'] != '0':
            ip_addr = socket.gethostbyname(target)
            if res['scan'][ip_addr]['tcp'][int(ports)]['state'] == 'open':
                port_status = "OPEN"
                port_service = res['scan'][ip_addr]['tcp'][int(ports)]['name']
                service_version = res['scan'][ip_addr]['tcp'][int(ports)]['product'] + " " +  res['scan'][ip_addr]['tcp'][int(ports)]['version']
        else:
             port_status = "CLOSED"
             port_service = "Nil"
             service_version = "Nil"

        scan_info = {'scan_type':'Port Scan',
                     'scan_method':'Custom Scan',
                     'port_status':port_status,
                     'port_service':port_service,
                     'service_version':service_version}

        out = {'res':res,'scan_info':scan_info}
        return render(request,'result.html',out)
    return render(request,'custom_scan.html')


def advanced_scan(request):
    
    return render(request,'advanced_scan.html')

def ping_scan(request):
    if request.method == 'POST':
        target = request.POST['targets']

        res = scanner.scan(hosts=target,arguments='-sn')
        print(res)
        return render(request,'result.html',{'res':res})
    return render(request,'ping_scan.html')

def tcp_scan(request):
    if request.method == 'POST':
        target = request.POST['targets']
        port = request.POST['ports']

        res = scanner.scan(target,port,arguments='-sS')
        return render(request,'result.html',{'res':res})
    return render(request,"tcp_scan.html")

def udp_scan(request):
    if request.method == 'POST':
        target = request.POST['targets']
        port = request.POST['ports']

        res = scanner.scan(target,port,'-sU')
        return render(request,'result.html',{'res':res})
    return render(request,"udp_scan.html")

def stealth_scan(request):
    if request.method == 'POST':
        target = request.POST['targets']
        port = request.POST['ports']

        res = scanner.scan(target,port,arguments='-sS')
        return render(request,'result.html',{'res':res})
    
    return render(request,"stealth_scan.html")

def aggressive_scan(request):
    if request.method == 'POST':
        target = request.POST['targets']
        port = request.POST['ports']

        scanner = nmap.PortScanner()
        res = scanner.scan(hosts=target,arguments='-A')
        return render(request,"result.html",{'res':res})
    return render(request,"aggressive_scan.html")

def full_scan(request):
    if request.method == 'POST':
        target = request.POST['targets']

        res = scanner.scan(hosts=target,arguments='-p0-65535')
    return render(request,"full_scan.html")

def my_scan(request):
    return render(request,'my_scan.html')