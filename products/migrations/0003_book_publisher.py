# Generated by Django 3.2 on 2022-07-03 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_name_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(default='exit', max_length=100),
            preserve_default=False,
        ),
    ]
