# Generated by Django 4.0.3 on 2023-02-10 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageItems', '0009_authentication'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='category',
            field=models.CharField(choices=[('Student', 'Teacher')], max_length=20, null=True),
        ),
    ]