# Generated by Django 4.1.3 on 2022-11-07 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]