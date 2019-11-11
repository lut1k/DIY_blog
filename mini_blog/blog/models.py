from django.db import models
from datetime import date
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User #Blog author or commenter

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    bio = models.TextField(max_length=400, help_text="Enter your bio details here")
    date_birth = models.DateField(auto_now=False)

    def __str__(self):
        return self.surname + " " + self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular blog-author instance.
        """
        return reverse('blogs-by-author', args=[str(self.pk)])


class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    publication_date = models.DateField(default=date.today)
    description = models.TextField(max_length=2000, help_text="Enter you blog text here")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular blog instance.
        """
        return reverse('blog-detail', args=[str(self.pk)])

    class Meta:
        ordering = ["-publication_date"]

    objects = models.Manager()


class Comment(models.Model):
    post_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=1000, help_text="Enter you comment about blog here")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        len_title = 75
        if len(self.description) > len_title:
            titlestring = self.description[:len_title] + '...'
        else:
            titlestring = self.description
        return titlestring
