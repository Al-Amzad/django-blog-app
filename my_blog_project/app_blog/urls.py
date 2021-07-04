from django.urls import path
from app_blog import views

app_name = 'app_blog'

urlpatterns = [
	path ('', views.BlogList.as_view(), name = 'blog_list'),
	path ('write/', views.CreateBlog.as_view (), name = 'create_blog'),
	path ('details/<slug:slug>', views.blog_details, name = 'blog_details'),
]
