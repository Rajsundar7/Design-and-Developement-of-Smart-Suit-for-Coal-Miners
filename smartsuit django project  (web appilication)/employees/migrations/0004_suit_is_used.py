# Generated by Django 4.1 on 2022-08-25 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_employee_is_suited'),
    ]

    operations = [
        migrations.AddField(
            model_name='suit',
            name='is_used',
            field=models.BooleanField(default=False),
        ),
    ]
