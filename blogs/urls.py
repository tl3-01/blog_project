"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that show all blog posts.
    path('blog_posts/', views.blog_posts, name='blog_posts'),
    # Page that show individual blot post.
    path('blog_posts/<int:blog_post_id>/', views.blog_post, name='blog_post'),
    # Page for adding a new post.
    path('new_post/', views.new_post, name='new_post'),
    # Page for editing a post.
    path('edit_post/<int:blog_post_id>', views.edit_post, name='edit_post'),
    # Page for delete a post.
    path('delete_post/<int:blog_post_id>/delete/', views.delete_post,
        name='delete_post'), 
    # Page for adding a new content for post.
    path('new_content/<int:blog_post_id>/', views.new_content,
        name='new_content'),
    # Page for editing a content.
    path('edit_content/<int:content_id>/', views.edit_content,
        name='edit_content'),
    # Page for delete a content.
    path('delete_content/<int:content_id>/delete/', views.delete_content,
        name='delete_content'),
]
