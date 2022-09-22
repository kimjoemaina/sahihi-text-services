# Django Imports
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.core.paginator import Paginator

# Other imports
from .models import PortfolioItem, TeamMember, BlogPost
from .forms import ContactForm


# Create your views here.
def home(request):
    try:
        portfolio_items = PortfolioItem.objects.all()
        team_members = TeamMember.objects.all()
        form = ContactForm(request.POST)

        if request.method == 'POST':
            if form.is_valid():
                subject = form.cleaned_data['subject']
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                phone_no = form.cleaned_data['phone_no']
                message = form.cleaned_data['message']
                
                html = render_to_string('contactform.html',
                    {
                        'subject' : subject,
                        'name' : name,
                        'email': email,
                        'phone_no': phone_no,
                        'message' : message
                    }
                )

                send_mail(subject, message, email,['kimanijmaina@gmail.com'], html_message=html)
                return redirect('home')
            else:
                form = ContactForm()

        context = {
            'portfolio_items' : portfolio_items,
            'team_members' : team_members,
            'form': form
        }

        return render(request, 'index.html', context)
    except PortfolioItem.DoesNotExist or TeamMember.DoesNotExist:
        return render(request, 'index.html')
    
def blog(request):
    blog_posts = BlogPost.objects.all()
    paginator = Paginator(blog_posts, 5)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    context = {
        'blog_posts' : posts
    }

    return render(request, 'blog/blog.html', context)

def article(request, slug):

    post = get_object_or_404(BlogPost, slug=slug)
    
    context = {
        'post' : post
    }

    return render(request, 'blog/post.html', context)

def error_404(request, exception, template_name='404.html'):
    context = {

    }
    return render(request, '404.html', context)

# def error_500(request, template_name='500.html'):
#     context = {

#     }
#     return render(request, '500.html')