# Generated by Django 4.2 on 2024-04-08 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('code', models.CharField(blank=True, editable=False, max_length=16, null=True)),
                ('site_map', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
