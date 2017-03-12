# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WritePost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date_posted', models.DateField(blank=True, null=True)),
                ('blog_post', models.CharField(max_length=3000)),
                ('post_author', models.CharField(max_length=50)),
            ],
        ),
    ]
