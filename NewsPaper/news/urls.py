from django.urls import path
from .views import (
    PostList, PostDetail, PostCreateView, PostUpdateView, PostDeleteView, PostSearch,
    subscriptions
)

from .views import  CategoryListView, subscribe, unsubscribe

from django.views.decorators.cache import cache_page



urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', cache_page(60)(PostList.as_view()), name='post_list'),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', cache_page(60*5)(PostDetail.as_view()), name='post_detail'),
   path('create/', PostCreateView.as_view(), name='article_add'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
   path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
   path('subscriptions/', subscriptions, name='subscriptions'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
   path('categories/<int:pk>/unsubscribe', unsubscribe, name='unsubscribe'),
]