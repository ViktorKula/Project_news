# Generated by Django 5.0.1 on 2024-04-17 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_alter_category_thematic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='thematic',
            field=models.CharField(choices=[('GS', 'Gossip'), ('PO', 'Politics'), ('TH', 'Technology'), ('BL', 'Breaking')], help_text='category name', max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='thematic_en_us',
            field=models.CharField(choices=[('GS', 'Gossip'), ('PO', 'Politics'), ('TH', 'Technology'), ('BL', 'Breaking')], help_text='category name', max_length=2, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='thematic_ru',
            field=models.CharField(choices=[('GS', 'Gossip'), ('PO', 'Politics'), ('TH', 'Technology'), ('BL', 'Breaking')], help_text='category name', max_length=2, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
