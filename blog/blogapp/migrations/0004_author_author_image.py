# Generated by Django 3.2.5 on 2022-08-28 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_author_author_biodata'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='author_image',
            field=models.ImageField(blank=True, null=True, upload_to='authors/'),
        ),
    ]
