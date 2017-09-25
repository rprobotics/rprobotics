#!/usr/bin/env python

from units import unit
import units.predefined
import gzip
import psycopg2



pantry_list = {'chicken': {'quantity': unit('lb')(2)},
               'eggs': {'quantitiy': unit('count')(24)},
               'potatoes': {'quantitiy': unit('count')(4)},
               'celery': {'quantitiy': unit('count')(4)},
               'tomatoes': {'quantitiy': unit('lb')(1)},
               'bacon': {'quantitiy': unit('lb')(.5)},
               'lettuce': {'quantitiy': unit('lb')(1.5)},
               'ground turkey': {'quantitiy': unit('lb')(2)}
               'noodles': {'quantitiy': unit('count')(4)},
               'butter': {'quantitiy': unit('oz')(24)},
               'bbq sauce': {'quantitiy': unit('oz')(48), 'synonyms': ['barbcue sauce'] }

               }

#               '': {'quantitiy': unit('')()},
#               '': {'quantitiy': unit('')()},


if __name__ == '__main__':
    units.predefined.define_units()
    conn = psycopg2.connect("dbname=docker user=docker")
    cur = conn.cursor()



