# Generated by Django 3.0.5 on 2020-04-07 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pround',
            field=models.TextField(blank=True, verbose_name='Pround'),
        ),
    ]
