# Generated by Django 2.2 on 2020-07-29 02:53

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_time']},
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
