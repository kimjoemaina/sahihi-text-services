from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog/blog.html')

def post(request):
    return render(request, 'blog/post.html')