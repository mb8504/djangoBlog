# Generated by Django 5.0.3 on 2024-04-10 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_postseries_post_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcategory',
            name='path',
            field=models.CharField(default=1, max_length=200),
        ),
    ]