# Generated by Django 3.2.5 on 2021-08-14 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppReview', '0003_alter_ticket_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userfollows',
            options={'verbose_name_plural': 'UsersFollows'},
        ),
    ]