# Generated by Django 3.2.8 on 2021-10-28 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_alter_postcomment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='postforum',
            name='asParent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.postforum'),
        ),
    ]