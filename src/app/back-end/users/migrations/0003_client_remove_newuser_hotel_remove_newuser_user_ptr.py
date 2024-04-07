# Generated by Django 4.2 on 2024-03-18 16:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_newuser_hotel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_guest', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
            ],
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='user_ptr',
        ),
    ]