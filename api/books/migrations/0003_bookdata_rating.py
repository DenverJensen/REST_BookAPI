# Generated by Django 4.1.3 on 2022-11-01 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_bookdata_duration_remove_bookdata_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdata',
            name='rating',
            field=models.CharField(default='', max_length=1),
            preserve_default=False,
        ),
    ]