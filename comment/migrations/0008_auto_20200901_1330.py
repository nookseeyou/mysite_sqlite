# Generated by Django 2.2 on 2020-09-01 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0007_merge_20200901_1330'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['comment_time']},
        ),
    ]
