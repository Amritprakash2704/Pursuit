# Generated by Django 4.1.1 on 2022-11-29 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pursuit_app', '0024_alter_interview_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview_marks',
            name='interview_score',
            field=models.PositiveIntegerField(verbose_name='interview_score'),
        ),
    ]
