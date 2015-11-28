# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(verbose_name='Імя', max_length=256)),
                ('last_name', models.CharField(verbose_name='Прізвище', max_length=256)),
                ('middle_name', models.CharField(verbose_name='По-батькові', blank=True, default='', max_length=256)),
                ('birthday', models.DateField(verbose_name='Дата  народження', null=True)),
                ('photo', models.ImageField(verbose_name='Фото', null=True, upload_to='', blank=True)),
                ('ticket', models.CharField(verbose_name='Білет', max_length=256)),
                ('notes', models.TextField(verbose_name='Додаткові  нотатки', blank=True)),
            ],
        ),
    ]
