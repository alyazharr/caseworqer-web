# Generated by Django 3.2.8 on 2021-10-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipskarier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipskarier',
            name='Cover',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]