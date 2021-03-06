# Generated by Django 2.0.4 on 2018-04-15 20:49

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignedto',
            name='task',
        ),
        migrations.RemoveField(
            model_name='assignedto',
            name='user',
        ),
        migrations.AddField(
            model_name='task',
            name='assignedTo',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='task_description',
            field=models.CharField(default=django.utils.timezone.now, max_length=512),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='task_text',
            field=models.CharField(max_length=64),
        ),
        migrations.DeleteModel(
            name='AssignedTo',
        ),
    ]
