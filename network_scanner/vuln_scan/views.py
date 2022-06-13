from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import nmap
# Create your views here.



def vuln_home(request):
    return render(request,'vuln_index.html')

def vuln_scan(request):
    if request.method == 'POST':
        target = request.POST[target]

    
        scanner = nmap.PortScanner()

        res = scanner.scan(target,arguments="-sV --script=http-methods")
        return render(request,'result.html',{'res':res})
    return render(request,'vuln_scan.html')
