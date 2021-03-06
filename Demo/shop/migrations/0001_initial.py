# Generated by Django 3.2.9 on 2021-12-18 20:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_A',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'catgory_A',
                'verbose_name_plural': 'categories_A',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Category_B',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('category_A', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category_a')),
            ],
            options={
                'verbose_name': 'catgory_B',
                'verbose_name_plural': 'categories_B',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='media/product_picture/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_B', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category_b')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
