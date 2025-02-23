from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
def index(request):

  posts = Post.objects.all()

  return render(request, 'blog/pages/index.html', {'posts': posts,})

def post(request, post_title, id):
  post = get_object_or_404(Post, id=id)

  context = {
    "post": post,
  }

  return render(request, 'blog/pages/post.html', context)