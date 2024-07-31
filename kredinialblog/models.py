from django.db import models
from django.contrib.auth.models import User
from slugify import slugify
from cloudinary.models import CloudinaryField 

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    cover_image = CloudinaryField('image', blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def author_full_name(self):
        return f"{self.author.first_name} {self.author.last_name}"

    def get_categories(self):
        return ", ".join([category.name for category in self.categories.all()])

# models.py
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Yeni alanlar
    author_first_name = models.CharField(max_length=30, blank=True)
    author_last_name = models.CharField(max_length=30, blank=True)

    def save(self, *args, **kwargs):
        self.author_first_name = self.author.first_name
        self.author_last_name = self.author.last_name
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Comment by {self.author.get_full_name()} on {self.post.title}"
