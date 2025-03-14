# Generated by Django 5.1.6 on 2025-02-21 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AddField(
            model_name='post',
            name='favicon',
            field=models.ImageField(blank=True, default=None, upload_to='posts/favicon'),
        ),
    ]
