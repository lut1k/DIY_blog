from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home),
    re_path(r'^blogs/$', views.BlogListView.as_view(), name='blogs'),
    re_path(r'^bloggers/$', views.bloggers, name='bloggers'),
    re_path(r'^<int:pk>/$', views.BlogDetailView.as_view(), name="blog-detail")
]
