# Generated by Django 2.1 on 2020-07-12 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0004_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='created_date',
        ),
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
