# Generated by Django 2.1 on 2020-07-11 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0003_auto_20200711_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('mobile', models.BigIntegerField(blank=True, null=True)),
                ('created_date', models.DateField(auto_now=True, null=True)),
            ],
        ),
    ]
