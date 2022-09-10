from curses.ascii import HT
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1> JPEG Panic </h1>")
    my_context = {
        "article" : "solana article 1",
        "likes" : 12,
        "my_list" : ["degods", "blocksmith", "primates"]
    }
    return render(request, "home.html", my_context)

def polls_view(request, *args, **kwargs):
    return render(request, "polls.html", {})

def tweets_view(request, *args, **kwargs):
    return render(request, "tweets.html", {})