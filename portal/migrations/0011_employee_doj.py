# Generated by Django 2.0 on 2018-12-24 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_auto_20181223_0441'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='DOJ',
            field=models.DateField(blank=True, null=True, verbose_name='Date Of Joining.'),
        ),
    ]