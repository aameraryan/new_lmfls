# Generated by Django 2.1.4 on 2019-01-04 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0014_auto_20181227_0319'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValueModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Short_Name', models.CharField(max_length=5)),
                ('Point', models.FloatField(default=0.0)),
                ('Fixed_Name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='attendance',
            name='Value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.ValueModel', verbose_name='value'),
        ),
    ]