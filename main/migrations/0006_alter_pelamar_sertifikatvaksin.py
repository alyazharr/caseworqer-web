# Generated by Django 3.2.8 on 2021-10-22 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_pelamar_idlowongan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelamar',
            name='sertifikatVaksin',
            field=models.TextField(),
        ),
    ]