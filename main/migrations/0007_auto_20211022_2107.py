# Generated by Django 3.2.8 on 2021-10-22 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_pelamar_sertifikatvaksin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelamar',
            name='company',
        ),
        migrations.RemoveField(
            model_name='pelamar',
            name='jobs',
        ),
    ]