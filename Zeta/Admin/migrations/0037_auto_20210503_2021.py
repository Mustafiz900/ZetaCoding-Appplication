# Generated by Django 3.0.8 on 2021-05-03 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0036_auto_20210503_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referrer_profile',
            name='Rf_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stud_profile',
            name='stud_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trainer_profile',
            name='tr_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
