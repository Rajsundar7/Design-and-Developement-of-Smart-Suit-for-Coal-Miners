# Generated by Django 4.1 on 2022-08-26 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_remove_suit_is_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateField(),
        ),
    ]
