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

    def dispatch(self, request, *args, **kwargs):
        self.form = forms.BlogListForm(request.GET)
        self.form.is_valid()
        return super(BlogListView, self).dispatch(request, *args, **kwargs)
        
    def get_queryset(self):
        queryset = models.Blog.objects.all()
        if self.form.cleaned_data.get('search'):
            queryset = queryset.filter(title__icontains=self.form.cleaned_data['search'])
        if self.form.cleaned_data.get('sort_field'):
            queryset = queryset.order_by(self.form.cleaned_data['sort_field'])
        return queryset
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context


def bloggers(request):
    return HttpResponse("Func bloggers")


# class BlogDetailView(generic.DetailView):
#     """
#     Generic class-based detail view for a blog.
#     """
#     model = models.Blog

# class AllBloggsView(generic.ListView):
#     model = models.Blog
#
#     def get(self, request):
#         context = {
#             "blog_list": self.model,
#         }
#         return render(request, "blog_list.html", context)


