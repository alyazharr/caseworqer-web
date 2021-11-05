# Generated by Django 3.2.8 on 2021-11-05 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='perusahaanKomen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('postTime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date published')),
                ('pekerjaan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.lowongankerja')),
                ('penulis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('pekerjaan', 'penulis')},
            },
        ),
    ]
