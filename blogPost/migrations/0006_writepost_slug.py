# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0005_remove_writepost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='writepost',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, default='pblog'),
        ),
    ]
