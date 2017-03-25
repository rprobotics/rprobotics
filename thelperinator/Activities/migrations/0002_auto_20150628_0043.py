# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Activities', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activitytype',
            old_name='activity',
            new_name='name',
        ),
    ]
