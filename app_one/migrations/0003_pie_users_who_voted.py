# Generated by Django 4.2.1 on 2023-06-13 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_pie'),
    ]

    operations = [
        migrations.AddField(
            model_name='pie',
            name='users_who_voted',
            field=models.ManyToManyField(related_name='liked_pies', to='app_one.user'),
        ),
    ]
