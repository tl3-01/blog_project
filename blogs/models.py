from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    """List of the blog sites."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the blog post."""
        return self.text

class Content(models.Model):
    """Individual post page direct from Homepage."""
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a simple string representing the blog post."""
        if len(self.text) > 50:
            return f"{self.text[:50]}"
        else:
            return f"{self.text}"
