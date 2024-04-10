from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import MinValueValidator

from django.core.cache import cache

from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy # импортируем «ленивый» геттекст с подсказкой

arcticle = 'AR'
news = 'NW'

TYPE = [
    (arcticle, 'Статья'),
    (news, 'Новость')
]


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        self.author_rating = 0
        for post in Post.post_rating.validators:
            self.author_rating += post * 3
        for comment in Comment.comment_rating.validators:
            self.author_rating += comment
        self.save()

    def username(self):
        return self.user.username
    def __str__(self):
        return self.user.username

class Category(models.Model):

    #category_name = models.CharField(max_length=255, unique=True)

    gossip = 'GS'
    policy = 'PO'
    technology = 'TH'
    bullet = 'BL'

    TEMATIC = [
        (gossip, 'СВЕТСКИЕ НОВОСТИ'),
        (policy, 'ПОЛИТИКА'),
        (technology, 'ТЕХНИКА'),
        (bullet, 'СРОЧНЫЕ НОВОСТИ')
    ]
    thematic = models.CharField(max_length=2, choices=TEMATIC, unique=True, help_text=_('category name'))
    subscribers = models.ManyToManyField(User, blank=True, related_name='categories')

    def __str__(self):
        return self.get_thematic_display()

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    kind = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='kinds',
        verbose_name=pgettext_lazy('help text for MyModel model', 'This is the help text'),
    )

post = 'PO'
news = 'NE'
POST = [
    (post, 'ПОСТ'),
    (news, 'НОВОСТЬ')
]

class Post(models.Model):
    post_author = models.ForeignKey('Author', on_delete=models.CASCADE)
    post_choice = models.CharField(max_length=2,
                                   choices=TYPE,
                                   default=news)
    post_date = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField('Category', through='PostCategory')
    post_title = models.CharField(max_length=30)
    post_text = models.TextField()
    post_rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.post_title.title()}: {self.post_text[:10]}'

    def preview(self):
        preview = self.post_text[0:125] + '...'
        return preview

    def like(self, amount=1):
        self.post_rating += amount
        self.save()

    def dislike(self, amount=1):
        self.post_rating -= amount
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'post-{self.pk}')



class PostCategory(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category}'



class Comment(models.Model):
    comment_post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_date = models.DateTimeField()
    comment_rating = models.IntegerField(default=0)

    def like(self, amount=1):
        self.comment_rating += amount
        self.save()

    def dislike(self, amount=1):
        self.comment_rating -= amount
        self.save()


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2",)
class NewsPortalCategory(models.Model):
    news_category = models.ForeignKey(Post, on_delete=models.CASCADE)
    news_portal = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Create your models here.


class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
