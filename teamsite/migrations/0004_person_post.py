# Generated by Django 4.1.5 on 2023-01-31 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamsite', '0003_alter_person_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='post',
            field=models.CharField(default='', max_length=256),
        ),
    ]