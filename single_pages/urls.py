from django.urls import path
from . import views

urlpatterns = [
  path('about_me/', views.about_me),
  path('app-ads.txt',views.AppAds),
  path('ads.txt',views.Ads),
  path('robots.txt', views.robot),
  path('naver523e858e1b8d55b7a49dc373b86473f0.html', views.naver),
  path('', views.landing),
]
