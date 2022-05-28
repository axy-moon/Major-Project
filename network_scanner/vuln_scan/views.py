from django.shortcuts import render

# Create your views here.

def vuln_home(request):
    return render(request,'vuln_index.html')