from post.models import Post
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView

# Create your views here.

class PostListView(ListView):
    template_name = "postlist.html"
    model = Post


class PostDetailView(DetailView):
    template_name = 'postdetail.html'

    def get_object(self):
        pk = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk)
        return post