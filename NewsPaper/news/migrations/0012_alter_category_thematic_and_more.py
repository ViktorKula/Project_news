# Generated by Django 5.0.1 on 2024-04-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_alter_category_thematic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='thematic',
            field=models.CharField(choices=[('GS', 'СВЕТСКИЕ НОВОСТИ'), ('PO', 'ПОЛИТИКА'), ('TH', 'ТЕХНИКА'), ('BL', 'СРОЧНЫЕ НОВОСТИ')], help_text='Имя категории', max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='thematic_en_us',
            field=models.CharField(choices=[('GS', 'СВЕТСКИЕ НОВОСТИ'), ('PO', 'ПОЛИТИКА'), ('TH', 'ТЕХНИКА'), ('BL', 'СРОЧНЫЕ НОВОСТИ')], help_text='Имя категории', max_length=2, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='thematic_ru',
            field=models.CharField(choices=[('GS', 'СВЕТСКИЕ НОВОСТИ'), ('PO', 'ПОЛИТИКА'), ('TH', 'ТЕХНИКА'), ('BL', 'СРОЧНЫЕ НОВОСТИ')], help_text='Имя категории', max_length=2, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_choice',
            field=models.CharField(choices=[('AR', 'Статья'), ('NW', 'Новость')], default='NW', max_length=2),
        ),
    ]
