from django.shortcuts import render
from .models import PortfolioItem

# Create your views here.
def home(request):
    try:
        portfolio_items = PortfolioItem.objects.all()
        context = {
                'portfolio_items' : portfolio_items
            }
        return render(request, 'index.html', context)
    except PortfolioItem.DoesNotExist:
        return render(request, 'index.html')
    
def blog(request):
    return render(request, 'blog/blog.html')

def post(request):
    return render(request, 'blog/post.html')