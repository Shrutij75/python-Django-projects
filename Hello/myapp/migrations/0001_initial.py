# Generated by Django 5.0.6 on 2024-05-25 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=12)),
                ('phone', models.CharField(max_length=12)),
                ('description', models.TextField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
    ]
