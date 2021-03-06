# Generated by Django 4.0.1 on 2022-01-15 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone_api', '0004_alter_medication_code_alter_medication_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='battery_capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='drone',
            name='serial_number',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
