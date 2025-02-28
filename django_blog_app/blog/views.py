from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator

# Create your views here.
def index(request):

  posts = Post.objects.all().order_by('-id')
  paginator = Paginator(posts, 5)
  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request, 'blog/pages/index.html', {'page_obj': page_obj,})

def post(request, post_title, id):
  post = get_object_or_404(Post, id=id)

  context = {
    "post": post,
  }

  return render(request, 'blog/pages/post.html', context)