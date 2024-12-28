from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def posts(request):
    return render(request, 'blog/all-posts.html')

def post_details(request, slug):
    return HttpResponse(f"Hello, world. You're at the blog post {slug}.")