# Generated by Django 3.2.6 on 2021-09-04 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.TextField(default=None, max_length=32),
            preserve_default=False,
        ),
    ]
