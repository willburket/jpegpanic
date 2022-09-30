import imp
from urllib import response
from django.shortcuts import render
from .models import Article, Comment
from .scrape import daily_hodl_scraper
from .forms import CommentForm
from django.views.generic import View, TemplateView
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import loader


# Create your views here.
def article_detail_view(request):
    obj = Article.objects.latest('date')

    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        form = CommentForm()

    context = {
        'object': obj,
        'form': form
    }
    return render(request, "article/article_detail.html", context)

def article_home_view(request):
    articles = []

    daily_hodl_scraper(1)
    # latest = Article.objects.filter(source__iexact = 'dailyhodl').latest('date')  

    articles = Article.objects.all().order_by('-date')[:10] 

    context = {
        'articles': articles,   
    }

    return render(request, "article/article_home.html", context)

class MainView(TemplateView):
    
    template_name = 'article/article_home.html'

class ArticleJsonListView(View):
    daily_hodl_scraper(1)
    def get(self, *args, **kwargs):
        print(kwargs)
        upper = kwargs.get('num_articles')
        lower = upper - 9
        articles_size = len(Article.objects.all())
        max_size = True if upper >= articles_size else False
        articles = list(Article.objects.values()[lower:upper])
        return JsonResponse({'data': articles, 'max': max_size}, safe=False)



