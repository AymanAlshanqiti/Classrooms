# Generated by Django 2.1.5 on 2019-02-17 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_auto_20190217_1647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='date_of_bith',
            new_name='date_of_birth',
        ),
    ]
