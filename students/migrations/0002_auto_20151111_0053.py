# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Назва', max_length=256)),
                ('notes', models.TextField(verbose_name='Додаткові  нотатки', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Групи',
                'verbose_name': 'Група',
            },
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'Студенти', 'verbose_name': 'Студент'},
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(null=True, blank=True, verbose_name='Староста', to='students.Student', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
