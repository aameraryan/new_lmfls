# Generated by Django 2.0 on 2018-12-24 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0012_month_leaves'),
    ]

    operations = [
        migrations.AddField(
            model_name='month_leaves',
            name='Added_Times',
            field=models.IntegerField(default=0),
        ),
    ]
