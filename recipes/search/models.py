# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
def get_ingredients(results):
    return results['ingredients']
    
def htmlize(html):
    results = ""
    for i in html:
        results += "{0}<br/><br/>".format(i)
    return results
    