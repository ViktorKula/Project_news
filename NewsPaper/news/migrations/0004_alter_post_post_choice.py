# Generated by Django 5.0.1 on 2024-02-20 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_choice',
            field=models.CharField(choices=[('article', 'Статья'), ('news', 'Новость')], default='news', max_length=10),
        ),
    ]