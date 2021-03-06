# Generated by Django 2.2 on 2018-08-15 12:13

from django.conf import settings
from django.db import migrations, models
import medium.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(default='medium/default.png', upload_to=medium.models.uploadMedium)),
                ('description', models.CharField(max_length=50, null=True)),
                ('isAvatar', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='timestamp')),
                ('user', models.ManyToManyField(related_name='user_medium', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'medium',
                'get_latest_by': 'date_uploaded',
            },
        ),
    ]
