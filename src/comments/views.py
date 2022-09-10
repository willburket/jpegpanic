from django.shortcuts import render
from .models import Comment
from .forms import CommentForm 

# Create your views here.
def comment_detail_view(request):
    obj = Comment.objects.get(id=1)
    # context = {
    #    'title': obj.title,
    #    'description': obj.description,
    #    'likes': obj.likes
    # }
    context = {
        'object': obj
    }
    return render(request, "comment/comment_detail.html", context)

# def comment_create_view(request):
#     form = RawCommentForm()
#     if request.method == "POST":
#         form = RawCommentForm(request.POST)
#         if form.is_valid():
#             # form.instance.user = request.user
#             Comment.user = request.user
#             # form.save()
#             print(form.cleaned_data)
#             Comment.objects.create(**form.cleaned_data)
#             form = RawCommentForm()
#         else:
#             print(form.errors)
            

#     context = {
#         'form': form
#     }
#     return render(request, "comment/comment_create.html", context)

def comment_create_view(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        form = CommentForm()
    
    context = {
        'form': form,
    }
    return render(request, "comment/comment_create.html", context)