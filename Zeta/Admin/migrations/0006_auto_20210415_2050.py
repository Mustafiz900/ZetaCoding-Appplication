# Generated by Django 3.0.8 on 2021-04-15 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_auto_20210413_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stud_detail',
            name='id',
        ),
        migrations.AlterField(
            model_name='stud_detail',
            name='Stud_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Admin.stud_profile'),
        ),
        migrations.AlterField(
            model_name='stud_profile',
            name='stud_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
