# Generated by Django 5.1.4 on 2025-02-21 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
