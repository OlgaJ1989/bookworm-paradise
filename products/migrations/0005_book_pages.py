# Generated by Django 3.2 on 2022-07-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_book_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]