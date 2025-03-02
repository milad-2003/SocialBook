# Generated by Django 5.1.4 on 2025-02-07 08:36

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='post_images')),
                ('caption', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('no_of_likes', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profile')),
            ],
        ),
    ]
