# Generated by Django 5.1.6 on 2025-02-22 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=400),
        ),
    ]
