from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import *

from .forms import PostForm
from .filters import PostFilter

from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.shortcuts import redirect, get_object_or_404, render
from django.views.decorators.csrf import csrf_protect


from django.core.cache import cache
# импортируем функцию для перевода
from django.utils.translation import gettext as _
# from django.utils.translation import activate, get_supported_language_variant, LANGUAGE_SESSION_KEY
# импортируем функцию для перевода

# Create your views here.

class Index(View):
    def get(self, request):
        # . Translators: This message appears on the home page only
        models = MyModel.objects.all()

        context = {
            'models': models,
        }

        return HttpResponse(render(request, 'flatpages/default.html', context))



class PostList(ListView):
    model = Post
    ordering = 'post_date'
    template_name = 'articles.html'
    context_object_name = 'post_news'
    paginate_by = 10

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса
        context = super().get_context_data(**kwargs)
        context['filterset'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем фильтр в контекст
        context['categories'] = PostCategory.objects.all()
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый пост
            form.save()

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    # def get(self, request):
    #     # . Translators: This message appears on the home page only
    #     models = Post.objects.all()
    #
    #     context = {
    #         'models': models,
    #     }
    #
    #     return HttpResponse(render(request, 'articles.html', context))


class PostDetail(DetailView):
    model = Post
    template_name = 'article.html'
    context_object_name = 'post_detail'

    def get_object(self, *args, **kwargs):  # переопределяем метод получения объекта
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)
        print ('--------------------------------')
        print (obj)
        print ('--------------------------------')
        # кэш очень похож на словарь, и метод get действует так же. Он забирает значение по ключу, если его нет, то забирает None.
        # если объекта нет в кэше, то получаем его и записываем в кэш
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)
        print('++++++++++++++++')
        print(obj)
        print('++++++++++++++++')
        return obj


class PostCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add.post')
    form_class = PostForm
    model = Post
    template_name = 'article_add.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.quantity = 10
        return super().form_valid(form)


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.update.post')
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'


# дженерик для удаления поста
class PostDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete.post',)
    model = Post
    template_name = 'article_delete.html'
    success_url = '/news/'



class PostSearch(ListView):  # поиск поста
    model = Post
    template_name = 'article_search.html'
    context_object_name = 'post_news'
    paginate_by = 5

    def get_queryset(self):  # получаем обычный запрос
        queryset = super().get_queryset()  # используем наш класс фильтрации
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class CategoryListView(PostList):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(post_category=self.category).order_by('-post_date')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context



@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)
    message = 'Вы подписались на категорию: '
    return render(request, 'subscribe.html', {'category': category, 'message': message})

@login_required
def unsubscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.remove(user)
    message = 'Вы отписались от категории: '
    return render(request, 'subscribe.html', {'category': category, 'message': message})

@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscription.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscription.objects.filter(
                user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscription.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('thematic')
    return render(
        request,
        'subscriptions.html',
        {'categories': categories_with_subscriptions},
    )


