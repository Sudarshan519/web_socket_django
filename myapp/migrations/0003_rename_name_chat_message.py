# Generated by Django 4.2.1 on 2023-06-08 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_chat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='name',
            new_name='message',
        ),
    ]
