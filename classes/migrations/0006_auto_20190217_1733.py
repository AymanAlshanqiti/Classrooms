# Generated by Django 2.1.5 on 2019-02-17 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_auto_20190217_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('GENDER', '-'), ('MALE', 'Male'), ('FEMALE', 'Female')], default='GENDER', max_length=10),
        ),
    ]
