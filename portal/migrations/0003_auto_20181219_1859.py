# Generated by Django 2.0 on 2018-12-19 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20181219_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AtDate', models.DateField(auto_now_add=True)),
                ('Value', models.FloatField(choices=[(1.0, 'Full Day'), (0.5, 'Half_Day'), (0.0, 'Absent')])),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Employee')),
            ],
        ),
        migrations.RemoveField(
            model_name='attendancee',
            name='User',
        ),
        migrations.DeleteModel(
            name='Attendancee',
        ),
    ]
