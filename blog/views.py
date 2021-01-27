from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import CommentForm


# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 2


# function comment post and pass admin for comment activate
# pass template => postdetail.html
# comment post for admin acceptance
# if admin accept comment it will show in frontpage either it will not show

def post_detail(request, slug):
    template_name = 'PostDetails.html'
    # search the post model
    # 404 mean not found
    post = get_object_or_404(Post, slug=slug)
    # post comment set comments filter isactive?
    comments = post.comments.filter(active=True)
    new_comment = None

    # if we get any comment post request then->
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)  # => Comment parameter pass new_comment
        if comment_form.is_valid():  # -> is valid comment
            new_comment = comment_form.save(commit=False)  # => comment save
            new_comment.post = post  # => post
            new_comment.save()
    else:
        comment_form = CommentForm()  # => empty comment set
    return render(request, template_name, {
        'post': post,
        'comments': comments,  # => old comments
        'new_comment': new_comment,  # => new comments waiting for acceptation
        'comment_form': comment_form  # => pass the form for comments
    })


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'PostDetails.html'
