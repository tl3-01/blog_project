from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost, Content
from .forms import BlogPostForm, ContentForm

# Create your views here.
def index(request):
    """The home page for blog."""
    return render(request, 'blogs/index.html')

@login_required
def blog_posts(request):
    """Show all blog posts."""
    posts = BlogPost.objects.filter(owner=request.user).order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/blog_posts.html', context)

@login_required
def blog_post(request, blog_post_id):
    """Show a single blog post and all of its contents."""
    post = BlogPost.objects.get(id=blog_post_id)
    check_post_owner(post, request.user)

    contents = post.content_set.order_by('-date_added')
    context = {'post': post, 'contents': contents}
    return render(request, 'blogs/blog_post.html', context)

@login_required
def new_post(request):
    """Add a new post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:blog_posts')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, blog_post_id):
    """Edit an existing post."""
    post = get_object_or_404(BlogPost, id=blog_post_id)
    check_post_owner(post, request.user)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog_posts')

    # Display a blank or invalid form.
    context = {'post':post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

@login_required
def delete_post(request, blog_post_id):
    """Delete an existing post."""
    post = get_object_or_404(BlogPost, id=blog_post_id)
    check_post_owner(post, request.user)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current content.
        form = BlogPostForm(instance=post)
    else:
        # POST data submitted; process data.
        post.delete()
        return redirect('blogs:blog_posts')

    context = {'post': post}
    return render(request, 'blogs/delete_post.html', context)

@login_required
def new_content(request, blog_post_id):
    """Add a new content for a particular post."""
    post = get_object_or_404(BlogPost, id=blog_post_id)
    check_post_owner(post, request.user)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ContentForm()
    else:
        # POST data submitted; process data.
        form = ContentForm(data=request.POST)
        if form.is_valid():
            new_content = form.save(commit=False)
            new_content.post = post
            new_content.save()
            return redirect('blogs:blog_post', blog_post_id=blog_post_id)

    # Display a blank or invalid form.
    context = {'post': post, 'form': form}
    return render(request, 'blogs/new_content.html', context)

@login_required
def edit_content(request, content_id):
    """Edit an existing content."""
    content = get_object_or_404(Content, id=content_id)
    post = content.post
    check_post_owner(post, request.user)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current content.
        form = ContentForm(instance=content)
    else:
        # POST data submitted; process data.
        form = ContentForm(instance=content, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog_post', blog_post_id=post.id)

    context = {'content': content, 'post': post, 'form': form}
    return render(request, 'blogs/edit_content.html', context)

@login_required
def delete_content(request, content_id):
    """Delete an existing content."""
    content = get_object_or_404(Content, id=content_id)
    post = content.post
    check_post_owner(post, request.user)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current content.
        form = ContentForm(instance=content)
    else:
        # POST data submitted; process data.
        content.delete()
        return redirect('blogs:blog_post', blog_post_id=post.id)

    context = {'content': content, 'post': post, 'form': form}
    return render(request, 'blogs/delete_content.html', context)

def check_post_owner(post, user):
    """Make sure the currently logged-in user owns the post that's 
    being requested.

    Raise Http404 error if the user does not own the post.
    """
    if post.owner != user:
        raise Http404
