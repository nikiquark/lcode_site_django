# Generated by Django 4.1.5 on 2023-01-31 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamsite', '0004_person_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='post',
            field=models.CharField(max_length=256),
        ),
    ]
