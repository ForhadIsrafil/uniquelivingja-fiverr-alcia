# Generated by Django 3.2.9 on 2021-11-09 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/home_slider')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='category_name',
        ),
        migrations.AddField(
            model_name='product',
            name='main_category',
            field=models.CharField(choices=[('Bathroom', 'Bathroom'), ('Kitchen', 'Kitchen'), ('Commercial', 'Commercial'), ('Hardware', 'Hardware')], default=('Bathroom', 'Bathroom'), max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.CharField(choices=[('Accessories', 'Accessories'), ('Showers', 'Showers'), ('Basin-Faucets', 'Basin-Faucets'), ('Toilets', 'Toilets'), ('Lighting', 'Lighting')], default=('Accessories', 'Accessories'), max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_sub_category',
            field=models.CharField(choices=[('Accessories', 'Accessories'), ('Showers', 'Showers'), ('Basin-Faucets', 'Basin-Faucets'), ('Toilets', 'Toilets'), ('Lighting', 'Lighting')], default=('Accessories', 'Accessories'), max_length=200, null=True),
        ),
    ]