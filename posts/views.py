from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
	posts = Post.objects.all()
	# SELECT * FROM posts_post
	# posts = Post.objects.get(id = 1)
	# SELECT * FROM posts_post WHERE id = 1
	# posts = Post.objects.filter(location = "台南")
	# SELECT * FROM posts_post WHERE location = "台南"

	
	return render(request, "posts/index.html", {"posts": posts})
	# return HttpResponse("My First Django App.")
