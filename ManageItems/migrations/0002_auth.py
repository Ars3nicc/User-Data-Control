# Generated by Django 4.0.3 on 2023-02-07 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageItems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]