from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post_list(request, year= None , month = None):
    if month is not None:
        return HttpResponse(f"Post List archive for {year} and {month} ")

    if year is not None:
        return HttpResponse(f"Post List archive for {year}")
    return HttpResponse('post list page')

def categories_list(request):
    return HttpResponse("category list page")

def post_detail(request, post_title):
    return HttpResponse(f"Post detail of {post_title}")

