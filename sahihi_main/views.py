from decimal import Context
from django.shortcuts import render
from .models import PortfolioItem, TeamMember

# Create your views here.
def home(request):
    try:
        portfolio_items = PortfolioItem.objects.all()
        team_members = TeamMember.objects.all()
        
        context = {
                'portfolio_items' : portfolio_items,
                'team_members' : team_members
            }

        return render(request, 'index.html', context)

    except PortfolioItem.DoesNotExist:
        return render(request, 'index.html')
    
def blog(request):
    return render(request, 'blog/blog.html')

def post(request):
    return render(request, 'blog/post.html')