# Generated by Django 3.0.2 on 2020-01-31 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uploads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=200)),
                ('created_time', models.DateTimeField()),
                ('test_type', models.CharField(max_length=300)),
            ],
        ),
    ]
