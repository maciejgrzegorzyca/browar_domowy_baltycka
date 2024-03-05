from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True, null=False)



class Blog_add(models.Model):
    blog_add_category = models.ForeignKey("blog.Category", on_delete=models.CASCADE, default=None, null=False)
    blog_title = models.CharField(max_length=26, null=True)
    blog_description = models.CharField(max_length=26, blank=True)