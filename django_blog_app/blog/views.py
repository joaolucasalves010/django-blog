from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from django.core.paginator import Paginator
from blog.forms import CustomRegisterForm, CustomLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='blog:login')
def index(request):
  posts = Post.objects.all().order_by('-id')
  paginator = Paginator(posts, 5)
  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request, 'blog/pages/index.html', {'page_obj': page_obj,})

@login_required(login_url='blog:login')
def post(request, post_author, id):
  post = get_object_or_404(Post, id=id)

  context = {
    "post": post,
  }

  return render(request, 'blog/pages/post.html', context)

def register(request):
  form = CustomRegisterForm()
  if request.user.is_authenticated:
    return redirect('blog:index')

  if request.method == "POST":
    form = CustomRegisterForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.save()
      return redirect('blog:login')

  return render(request, 'blog/pages/user_register.html', {'form': form})

def login_view(request):
  form = CustomLoginForm()
  if request.user.is_authenticated:
    return redirect('blog:index')

  if request.method == "POST":
    form = CustomLoginForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('blog:index')
    
  return render(request, 'blog/pages/user_login.html', {'form': form})


def logout_view(request):
  logout(request)
  return redirect('blog:login')