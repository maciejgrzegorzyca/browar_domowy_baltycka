from django.db import models

# Create your models here.
class Category(models.Model):
    # Fields
    category_name = models.CharField(max_length=20, unique=True, null=False)

    # Methods
    def __str__(self):
        return self.category_name
    

class Blog_add(models.Model):
    # Fields
    blog_add_category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, null=False)
    blog_title = models.CharField(max_length=26, null=True)
    blog_description = models.CharField(max_length=266, blank=True)

