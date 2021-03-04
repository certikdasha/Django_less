from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)


# Разрабатываем каталог книг, у каждой книги обязательно есть автор, и он может быть только один.
class Author(models.Model):
    name = models.CharField(max_length=120)


# Разработать книжную библиотеку. Храним книги, храним авторов, книгу могут написать несколько соавторов.
# храним кто брал книги, и доступна ли книга сейчас.
class Book(models.Model):
    name = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')


class BookUser(models.Model):
    name = models.CharField(max_length=120,  null=True)


class BookLibrary(models.Model):
    name = models.CharField(max_length=120)
    author_name = models.ManyToManyField(Author)
    book_user = models.ForeignKey(BookUser, on_delete=models.CASCADE, null=True, blank=True)


# Разработать набор моделей, для сайта-блога, на котором можно выставлять свои статьи,
# комментировать чужие, ставить лайк и дизлайк статье, и комментарию.
class BlogUser(models.Model):
    name = models.CharField(max_length=120)


class Post(models.Model):
    bl_user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)


class Comment(models.Model):
    bl_user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_to_comm = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)


class Like(models.Model):
    user_name = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class DisLike(models.Model):
    user_name = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class LikeCom(models.Model):
    user_name = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    comm = models.ForeignKey(Comment, on_delete=models.CASCADE)


class DisLikeCom(models.Model):
    user_name = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    comm = models.ForeignKey(Comment, on_delete=models.CASCADE)
