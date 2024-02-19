from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver


from .models import Post, PostCategory


@receiver(m2m_changed, sender=PostCategory)
def post_created(instance, **kwargs):

    emails = User.objects.filter(
        subscriptions__category__in=instance.post_category.all()
    ).values_list('email', flat=True)

    subject = f'Новый пост в категории "{instance.post_category}"'


    text_content = (
        f'Новый пост: {instance.post_title}\n'
        f'Ссылка на пост http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Новый пост: {instance.post_title}<br>'
        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        f'Ссылка на пост </a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()