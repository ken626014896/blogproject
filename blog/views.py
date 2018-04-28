from django.shortcuts import render
from django.http import  HttpResponse
from blog.models import Post


# Create your views here.
def  index(requset):
    articles=Post.objects.all()
    return  render(requset,"blog/index.html",{"articles":articles


                                              })