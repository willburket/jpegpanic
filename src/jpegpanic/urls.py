"""jpegpanic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view, polls_view, tweets_view
from articles.views import article_detail_view
from comments.views import comment_detail_view
from comments.views import comment_create_view
from articles.views import article_home_view
from articles.views import MainView, ArticleJsonListView
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings 



urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('articles-json/', ArticleJsonListView.as_view(), name = 'articles-json-view'),
    path('polls/', polls_view, name='polls'),
    path('tweets/', tweets_view, name='tweets'),
    path('articles/', article_home_view, name='articles'),
    path('admin/', admin.site.urls),
    path('comments/', comment_detail_view, name='comments'),
    path('create/', comment_create_view, name='create'),   
    
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
