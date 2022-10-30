from django.contrib import admin
from blogapp.models import Author, Blog, Book
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


@admin.action(description='Mark selected stories as published')
def make_published(modeladmin, request, queryset):
    queryset.update(blog_published=True)


class AuthorAdmin(admin.ModelAdmin):
    # displays all the components of a data instance
    list_display = ('author_first_name', 'author_last_name', 'author_email')
    # makes the data components clicakable
    list_display_links = ('author_first_name', 'author_last_name')
    # adds a filter bar to the right
    list_filter = list_display
    # adds a search bar
    search_fields = ['author_first_name', 'author_last_name']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_published',
                    'blog_create_date', 'blog_update_date', 'blog_author')
    # fields = (('blog_title', 'blog_published',
    #            'blog_author'), 'blog_content')
    # list_display_links = list_display
    fieldsets = (
        (
            # here, 'Blog details' is the heading of a section of fields
            'Blog Details', {
                # These fields will be in a single line, more aesthetically pleasing
                'fields': (('blog_title', 'blog_published',
                           'blog_author'),)
            }
        ),
        (
            'Content', {
                'fields': ('blog_content', 'blog_likes')
            }
        ),
    )
    list_filter = ('blog_title', 'blog_author')
    list_editable = ('blog_published',)
    actions = [make_published]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'book_author', 'book_isbn')
    list_display_links = ('book_title',)
    list_editable = ('book_author', 'book_isbn')


admin.site.register(Author, AuthorAdmin)
# admin.site.register(Blog, BlogAdmin)
