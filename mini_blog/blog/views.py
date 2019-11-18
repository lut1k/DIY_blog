from django.shortcuts import render, HttpResponse
from . import models
from . import forms
from django.views import generic
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    return render(request, "home.html")


class BlogListView(generic.ListView):
    """
    Generic class-based view for a list of all blogs.
    """
    model = models.Blog
    paginate_by = 5
    template_name = 'blog_list.html'


def bloggers(request):
    return HttpResponse("Func bloggers")


class BlogDetailView(generic.DetailView):
    """
    Generic class-based detail view for a blog.
    """
    model = models.Blog

# class AllBloggsView(generic.ListView):
#     model = models.Blog
#
#     def get(self, request):
#         context = {
#             "blog_list": self.model,
#         }
#         return render(request, "blog_list.html", context)


