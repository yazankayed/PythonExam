# Generated by Django 4.2.1 on 2023-06-13 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0003_pie_users_who_voted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pie',
            name='votes',
            field=models.TextField(default='0'),
        ),
    ]
