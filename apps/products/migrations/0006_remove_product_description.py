# Generated by Django 3.2.9 on 2021-11-09 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_homeslider_category_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]