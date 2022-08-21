from django.db import models
from sqlalchemy import false

# Create your models here.


class Author(models.Model):
    author_first_name = models.CharField(
        max_length=50, blank=False, help_text="Author's first name")
    author_last_name = models.CharField(
        max_length=50, blank=False, help_text="Author's Last name")
    author_email = models.EmailField(
        blank=False, unique=True, help_text='Author email id')

    def __str__(self) -> str:
        return self.author_first_name + ' ' + self. author_last_name
    # author's profile picture, bio, status, posts, followers, etc. can be added.


class Blog(models.Model):  # models.Model imports some special django-specific functions that allow us to manipulate DB
    blog_title = models.CharField(
        max_length=100, verbose_name='Blog Title', blank=False, help_text=' Enter Blog title. ')
    blog_content = models.TextField(
        max_length=2000, verbose_name='Blog Content', blank=False, help_text=' Write your blog here! ')
    blog_published = models.BooleanField(default=False)
    blog_create_date = models.DateTimeField(auto_now_add=True)
    blog_update_date = models.DateTimeField(auto_now=True)
    blog_author = models.ForeignKey(
        Author, on_delete=models.CASCADE, blank=False)

    def __str__(self) -> str:
        return self.blog_title


class Book(models.Model):
    book_title = models.CharField(max_length=50, blank=False)
    book_author = models.ForeignKey(
        Author, on_delete=models.CASCADE, blank=False)
    book_isbn = models.CharField(unique=True, blank=False, max_length=20)

    def __str__(self) -> str:
        return self.book_title
