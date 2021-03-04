from django.contrib import admin
from .models import Article, Author, Book, BookUser, BookLibrary, BlogUser, Post, Comment, Like, DisLike, LikeCom, \
    DisLikeCom


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article)

admin.site.register(Author)

admin.site.register(Book)

admin.site.register(BookUser)
admin.site.register(BookLibrary)

admin.site.register(BlogUser)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(DisLike)
admin.site.register(LikeCom)
admin.site.register(DisLikeCom)

