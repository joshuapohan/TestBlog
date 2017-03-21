# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0002_writepost_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='writepost',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, default='test1'),
            preserve_default=False,
        ),
    ]
