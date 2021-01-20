from django.db import models
from django.contrib.auth.models import User

Status = (
    (0, 'Unpublished'),
    (1, "Published"),
    (2, "Draft")
)


# Create your models here.
class Post(models.Model):
    # title, slug, author, updated_on, content, created_on, status
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE(), related_name="blog_post")
    updated_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=Status, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
