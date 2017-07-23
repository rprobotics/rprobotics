#!/usr/bin/env python



import json

json_output_array = []
output_file = open('fixtures/pantry.json', 'w')

counter = 1




new_pantry = { 'model': 'core.recipes', 'pk': counter, 'fields': {}}

json_output_array.append(new_pantry)

json.dump(json_output_array, output_file)
output_file.close()