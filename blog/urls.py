from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^blogs/$', views.BlogListView.as_view(), name='blogs'),
    re_path(r'^(?P<pk>\d+)/$', views.BlogDetailView.as_view(), name='blog-detail'),
    re_path(r'^bloggers/$', views.BlogerListView.as_view(), name='bloggers'),
    re_path(r'^blogger/(?P<pk>\d+)/$', views.BlogListbyAuthorView.as_view(), name='blogs-by-author'),
    re_path(r'^(?P<pk>\d+)/create/$', views.BlogCommentCreate.as_view(), name='blog-comment'),
]


