# Generated by Django 4.1.1 on 2022-11-02 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pursuit_app', '0012_alter_img_member_options_alter_img_member_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='img_member',
            options={},
        ),
        migrations.AlterModelManagers(
            name='img_member',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='img_member',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='img_member',
            name='email',
        ),
        migrations.RemoveField(
            model_name='img_member',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='img_member',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='img_member',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='img_member',
            name='user_permissions',
        ),
    ]
