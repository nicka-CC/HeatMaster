from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CalculatePriceForm, CustomUserCreationForm, CustomAuthenticationForm, CommentBlogForm, BlogForm, \
    ImageBlogForm
from .models import Thermostats, Blog, CommentBlog, ImageBlog


def home(request):
    thermostats = Thermostats.objects.all()
    return render(request, 'pages/home.html', {'thermostats': thermostats})
def thermoregulator(request):
    thermostats = Thermostats.objects.all()
    return render(request, 'pages/thermoregulator.html', {'thermostats': thermostats})

def about(request):
    return render(request, 'pages/about.html')
def calculate_price(request):
    if request.method == "POST":
        form = CalculatePriceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pages/calculate_price.html', context={'form_data': form.cleaned_data})
    else:
        form = CalculatePriceForm()
    return render(request, 'pages/calculate_price.html',{'form':form})

def signUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'pages/signUp.html', {'form': form})

def signIn(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'pages/signIn.html', {'form': form})
def blog(request):
    blogs = Blog.objects.prefetch_related("blod").all()
    return render(request, "pages/blog.html", {"blogs": blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog.objects.prefetch_related("blod"), id=blog_id)
    comments = CommentBlog.objects.filter(blog=blog).order_by('-date')

    if request.method == 'POST':
        form = CommentBlogForm(request.POST, user=request.user, blog=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', blog_id=blog_id)
    else:
        form = CommentBlogForm(user=request.user, blog=blog)

    return render(request, 'pages/blog_detail.html', {
        'blog': blog,
        'form': form,
        'comments': comments
    })
def create_blog(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)
        image_form = ImageBlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            blog_instance = blog_form.save()
            files = request.FILES.getlist('image_1')
            for file in files:
                image_instance = ImageBlog(image=file, blog=blog_instance, status='header')
                image_instance.save()
            return redirect('blog_detail', blog_id=blog_instance.id)
    else:
        blog_form = BlogForm()
        image_form = ImageBlogForm()
    return render(request, 'pages/create_blog.html', {
        'blog_form': blog_form,
        'image_form': image_form
    })

def videos(request):
    return render(request, 'pages/videos.html')