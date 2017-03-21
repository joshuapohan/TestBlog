# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0006_writepost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='writepost',
            name='absolink',
            field=models.CharField(max_length=150, default='test'),
            preserve_default=False,
        ),
    ]
