# Generated by Django 3.2.8 on 2021-10-21 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LowonganKerja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobs', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('jobType', models.CharField(max_length=10)),
                ('about', models.TextField()),
            ],
        ),
    ]
