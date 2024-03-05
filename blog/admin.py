from django.contrib import admin
from .models import Category, Blog_add


# Register your models here.
#class CategoryAdmin(admin.ModelAdmin):
 #   list_display = ('category_name',)


#admin.site.register(Category, CategoryAdmin)


#class BlogAdmin(admin.ModelAdmin):
#    list_display = ('blog_add_category', 'blog_title', 'blog_description')

#admin.site.register(Blog_add, BlogAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)



@admin.register(Blog_add)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog_add_category', 'blog_title', 'blog_description')