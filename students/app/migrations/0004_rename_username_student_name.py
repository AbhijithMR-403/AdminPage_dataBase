# Generated by Django 4.2 on 2023-08-12 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_name_student_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='username',
            new_name='name',
        ),
    ]
