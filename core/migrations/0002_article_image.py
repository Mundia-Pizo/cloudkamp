# Generated by Django 4.1.3 on 2022-11-29 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='new', upload_to='article-images'),
            preserve_default=False,
        ),
    ]