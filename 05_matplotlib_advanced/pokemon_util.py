import os
import numpy as np
import csv

POKENUM, MEGA, TYPE1, TYPE2, GEN, LEGENDARY = range(6)
TOTAL_STAT, HP, ATK, DEF, SPATK, SPDEF, SPD = range(6,13)
STAT_START = TOTAL_STAT

def is_mega(pokemon):
  if len(pokemon.split(' ')) > 1:
    return 'Mega' in pokemon.split(' ')[0]
  return False

"""
pokemon_name -> rest of array
"""
def load_pokemon(pokemon_fpath):
  poke_dict = {}
  headers = []
  type_set = set()

  with open(pokemon_fpath , 'r', encoding='cp932', errors='ignore') as f:
    headers = f.readline().strip().split(',')
    poke_headers = [headers[0], 'Mega'] + headers[2:4] + \
        headers[-2:] + headers[4:11]
    for line in csv.reader(f, quotechar='"', delimiter=',',
                               quoting=csv.QUOTE_MINIMAL):
      pokenum = int(line[0])
      pokename = line[1]
      mega = is_mega(pokename)
      poketype1, poketype2 = line[2:4]
      type_set.add(poketype1)
      if len(poketype2): type_set.add(poketype2)
      stats = [int(item) for item in line[4:11]]
      generation = int(line[-2])
      legendary = (line[-1] == 'True')

      poke_dict[pokename] = \
          [pokenum, mega, poketype1, poketype2, generation, legendary] + \
          stats
  poke_types = sorted(list(type_set))
  return poke_headers, poke_types, poke_dict

def poke_array(poke_dict, poke_types):
  type_dict = dict([(poke_type, i) for i, poke_type in enumerate(poke_types)])
  tups = []
  pokemon_by_number = sorted(list(poke_dict.keys()),
                key=lambda key: poke_dict[key][POKENUM])
  for pokemon in pokemon_by_number:
    poke_info = poke_dict[pokemon]
    mega_int, legend_int = int(poke_info[MEGA]), int(poke_info[LEGENDARY])
    poke_type1 = type_dict[poke_info[TYPE1]]
    poke_type2 = type_dict[poke_info[TYPE2]] if len(poke_info[TYPE2]) else -1
    tups.append([poke_info[POKENUM], int(poke_info[MEGA]), 
          poke_type1, poke_type2,
          poke_info[GEN], int(poke_info[LEGENDARY])] + poke_info[STAT_START:])
  poke_np_lookup = dict(enumerate(pokemon_by_number))
  return np.array(tups), poke_np_lookup
