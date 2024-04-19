# Generated by Django 5.0.3 on 2024-04-09 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_postcategory_post_path_postseries_post_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='series',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='blog.postseries', verbose_name='Series'),
        ),
    ]