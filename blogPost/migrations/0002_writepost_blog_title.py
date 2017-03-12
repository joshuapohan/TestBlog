# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='writepost',
            name='blog_title',
            field=models.CharField(max_length=300, default='placeholder'),
            preserve_default=False,
        ),
    ]
