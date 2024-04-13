# Generated by Django 5.0.1 on 2024-04-11 21:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_post_post_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='thematic_en_us',
            field=models.CharField(choices=[('GS', 'СВЕТСКИЕ НОВОСТИ'), ('PO', 'ПОЛИТИКА'), ('TH', 'ТЕХНИКА'), ('BL', 'СРОЧНЫЕ НОВОСТИ')], help_text='Имя категории', max_length=2, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='thematic_ru',
            field=models.CharField(choices=[('GS', 'СВЕТСКИЕ НОВОСТИ'), ('PO', 'ПОЛИТИКА'), ('TH', 'ТЕХНИКА'), ('BL', 'СРОЧНЫЕ НОВОСТИ')], help_text='Имя категории', max_length=2, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_author_en_us',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kinds', to='news.author', verbose_name='This is the help text'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_author_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kinds', to='news.author', verbose_name='This is the help text'),
        ),
        migrations.AlterField(
            model_name='category',
            name='thematic',
            field=models.CharField(choices=[('GS', 'СВЕТСКИЕ НОВОСТИ'), ('PO', 'ПОЛИТИКА'), ('TH', 'ТЕХНИКА'), ('BL', 'СРОЧНЫЕ НОВОСТИ')], help_text='Имя категории', max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kinds', to='news.author', verbose_name='This is the help text'),
        ),
    ]