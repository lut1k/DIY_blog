from django.shortcuts import render, HttpResponse
from . import models
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse


def home(request):
    return render(request, "index.html")


class BlogListView(generic.ListView):
    """
    Generic class-based view for a list of all blogs.
    """
    model = models.Blog
    paginate_by = 5


class BlogListbyAuthorView(generic.ListView):
    """
    Generic class-based view for a list of blogs posted by a particular BlogAuthor
    """
    model = models.Blog
    paginate_by = 5
    template_name = "blog/blog_list_by_author.html"

    def get_queryset(self):
        """
        Return list of Blog objects created by BlogAuthor (author id specified in URL)
        """
        target_author = get_object_or_404(models.BlogAuthor, pk=self.kwargs['pk'])
        return models.Blog.objects.filter(author=target_author)

    def get_context_data(self, **kwargs):
        """
        Add BlogAuthor to context so they can be displayed in the template
        """
        context = super(BlogListbyAuthorView, self).get_context_data(**kwargs)
        context['blogger'] = get_object_or_404(models.BlogAuthor, pk=self.kwargs['pk'])
        return context


class BlogerListView(generic.ListView):
    """
    Generic class-based view for a list of all blogs.
    """
    model = models.BlogAuthor
    paginate_by = 5


class BlogDetailView(generic.DetailView):
    """
    Generic class-based detail view for a blog.
    """
    model = models.Blog


class BlogCommentCreate(LoginRequiredMixin, CreateView):
    """
    Form for adding a blog comment. Requires login.
    """
    model = models.Comment
    fields = ['description']
    template_name = "blog/blogcomment_form.html"

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML
        """
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(models.Blog, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        """
        Add author and associated blog to form data befor setting it as valid (so it is saved to model)
        """
        form.instance.author = self.request.user
        form.instance.blog = get_object_or_404(models.Blog, pk=self.kwargs['pk'])
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'], })
