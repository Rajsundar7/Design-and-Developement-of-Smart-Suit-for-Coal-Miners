# Generated by Django 4.1 on 2022-08-25 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('dob', models.DateTimeField()),
                ('mobile', models.CharField(max_length=10)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender'), ('N', 'None')], default='N', max_length=11, null=True)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Suit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suit_id', models.CharField(max_length=10)),
                ('temperature', models.IntegerField(blank=True, null=True)),
                ('pressure', models.IntegerField(blank=True, null=True)),
                ('Methane', models.IntegerField(blank=True, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
            ],
        ),
    ]
