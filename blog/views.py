from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'pages/blog/blog-carousel.html')


def single(request):
    return render(request, 'pages/blog/blog-single-post.html')
