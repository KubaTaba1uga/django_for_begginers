# Generated by Django 3.2.7 on 2021-09-21 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
