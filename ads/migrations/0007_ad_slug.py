# Generated by Django 3.1.2 on 2021-12-14 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_ad_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
