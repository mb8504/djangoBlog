# Generated by Django 5.0.3 on 2024-04-09 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_series'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='series',
        ),
    ]
