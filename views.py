from django.shortcuts import render
from django.http import HttpResponse
import subprocess
# Create your views here.


def display_home(request):
    return render(request, 'Home.html')


def display_ide(request):
    process = subprocess.Popen(f'python C:/Users/adhis/PycharmProjects/pythonProject/Compiler.py', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return render(request, 'Home.html')


def display_feh(request):
    return render(request, 'FeHtml.html')


def display_fec(request):
    return render(request, 'FeCss.html')


def display_fej(request):
    return render(request, 'FeJs.html')


def display_bdj(request):
    return render(request, 'BeDjango.html')


def display_dms(request):
    return render(request, 'DbMysql.html')


def display_gh(request):
    return render(request, 'github.html')


def display_rp(request):
    return render(request, 'roadmap.html')


def display_fq1(request):
    return render(request, 'fequiz1.html')


def display_fa1(request):
    return render(request, 'feassign1.html')


def display_register(request):
    return render(request, 'register.html')


def display_login(request):
    return render(request, 'login.html')


def display_other(request):
    return render(request, 'other.html')



