# Generated by Django 5.0.3 on 2024-04-09 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.postseries', verbose_name='Series'),
        ),
    ]
