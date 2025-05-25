from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from blog.models import Post
from .models import Port
from datetime import datetime

# Create your views here.
def landing(request):
  recent_posts = Post.objects.order_by('-pk')[:3]
  return render(
    request,
    'single_pages/landing.html',
    {
      'recent_posts': recent_posts,
    }
  )

def about_me(request):
  ports = Port.objects.all().order_by('-time')
  age = datetime.today().year - 2000
  return render(
    request,
    'single_pages/about_me.html',
    {
      'ports': ports,
      'age':age
    }
  )


def AppAds(request):
    return HttpResponse("google.com, pub-5931873900368315, DIRECT, f08c47fec0942fa0")
      
def Ads(request):
    return HttpResponse("google.com, pub-5931873900368315, DIRECT, f08c47fec0942fa0")

def naver(request):
    return HttpResponse("naver-site-verification: naver523e858e1b8d55b7a49dc373b86473f0.html")
  
def robot(request):
    return HttpResponse(
    """
    User-agent: *
Allow:/
    """
    )
