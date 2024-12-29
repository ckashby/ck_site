from datetime import date
from django.shortcuts import render
from django.http import HttpResponse

posts = [
    { 'slug': 'hike-in-the-mountains', 
     'image': 'mountains.jpg', 
     'author': 'JP Smith', 
     'date': date.today(), # date(2021, 7, 21)
     'title': 'Hike in the Mountains',
      'excerpt': 'There\'s nothing like a day in the mountains.',
      'content': """
      Mountains are my favorite place to be. I go there every chance I get. The fresh air and the beautiful trees are a wonderful break from the city.
      
      There are many mountains to visit, but my favorite is the Black Mountain. It's the highest mountain in the state and the view from the top is amazing.
      
      When I hike in the mountains, I always take my camera with me. I love to take pictures of the beautiful scenery and the wildlife that lives there.
      
      If you've never been to the mountains, I highly recommend it. It's a great way to relax and get away from the hustle and bustle of everyday life.
      """
      },
]


def index(request):
    return render(request, 'blog/index.html')


def posts(request):
    return render(request, 'blog/all-posts.html')


def post_details(request, slug):
    # return HttpResponse(f"Hello, world. You're at the blog post {slug}.")
    return render(request, 'blog/post-detail.html')
