# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='test',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
