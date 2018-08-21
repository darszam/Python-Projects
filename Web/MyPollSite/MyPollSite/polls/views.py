from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def testsite(request):
    return HttpResponse("Hello, world. This is another polls test site.")