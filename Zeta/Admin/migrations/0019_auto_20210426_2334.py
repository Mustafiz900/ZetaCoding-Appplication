# Generated by Django 3.0.8 on 2021-04-26 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0018_auto_20210426_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stud_profile',
            name='stud_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trainer_profile',
            name='tr_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
