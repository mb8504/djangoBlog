# Generated by Django 5.0.3 on 2024-04-10 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_postcategory_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='series',
        ),
    ]
