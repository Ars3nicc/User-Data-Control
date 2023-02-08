# Generated by Django 4.0.3 on 2023-02-07 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageItems', '0002_auth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=50)),
                ('itemtype', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Auth',
        ),
    ]
