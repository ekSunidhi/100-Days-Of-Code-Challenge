from django.shortcuts import render

posts=[
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'contnet': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'contnet': 'Second post content',
        'date_posted': 'August 278, 2018'
    }
]

def home(request):
    context={
        'posts': posts
    }
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

