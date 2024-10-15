from django.views.generic import ListView, DetailView # type: ignore
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView): # type: ignore
    model = Post
    template_name = "post_detail.html"