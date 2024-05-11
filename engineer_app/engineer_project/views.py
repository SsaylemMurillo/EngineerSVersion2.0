from datetime import datetime
import math
from django.shortcuts import render, HttpResponse # type: ignore
from static.files.first_unit.procedures import *

# Create your views here.
def home(request):
    return render(request, "home.html")

# FIRST UNIT

def selector1(request):
    return render(request, "first_unit/selector1.html")

def first_unit_page1(request):
    return render(request, "first_unit/first_home.html")

def first_unit_page1_exce1(request):
    return render(request, "first_unit/subpages1/operation1.html")

# SECOND UNIT

def selector2(request):
    return render(request, "second_unit/selector2.html")

def second_unit_page1(request):
    return render(request, "second_unit/first_home.html")

def second_unit_page2(request):
    return render(request, "second_unit/second_home.html")

def second_unit_page3(request):
    return render(request, "second_unit/third_home.html")

def second_unit_page3_exce1(request):
    return render(request, "second_unit/subpages3/operation1.html")