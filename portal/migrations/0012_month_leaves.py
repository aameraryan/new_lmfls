# Generated by Django 2.0 on 2018-12-24 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_employee_doj'),
    ]

    operations = [
        migrations.CreateModel(
            name='Month_Leaves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Last_Added', models.DateField(blank=True, null=True)),
            ],
        ),
    ]