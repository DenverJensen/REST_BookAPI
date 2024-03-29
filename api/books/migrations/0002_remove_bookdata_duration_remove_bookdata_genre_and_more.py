# Generated by Django 4.1.3 on 2022-11-01 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookdata',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='bookdata',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='bookdata',
            name='rating',
        ),
        migrations.AddField(
            model_name='bookdata',
            name='category',
            field=models.CharField(default='favorites', max_length=200),
        ),
        migrations.AddField(
            model_name='bookdata',
            name='description',
            field=models.CharField(default='', max_length=5000),
            preserve_default=False,
        ),
    ]
