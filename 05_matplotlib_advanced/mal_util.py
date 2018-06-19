import os
import numpy as np
import csv

ANIME_ID, YEAR, SEASON, EPISODES, STUDIO, STUDIO_ADDTL = range(6)
SOURCE, SCORE, NUM_RATINGS, NUM_FAV = range(6,10)
SEASON_STRS = ['Winter', 'Spring', 'Summer', 'Fall']

def load_mal(mal_fpath):
  anime_dict = {}
  headers = []
  type_set = set()

  with open(mal_fpath, 'r') as f:
    headers = f.readline().strip().split(',')
    studios, sources = set(), set()
    for line in csv.reader(f, quotechar='"', delimiter=',',
                               quoting=csv.QUOTE_MINIMAL):
      animenum = int(line[0])
      animename = preprocess_name(line[1])
      show_type = line[4]
      if show_type != 'TV': # ignore all non-TV
        continue
      if line[2] == 'None': # not aired
        continue
      year, season = get_season(line[2])
      episodes = int(line[5])
      studio = line[8]
      if studio == '[]':
        continue
      source = line[9]
      score = float(line[10])
      num_ratings = int(line[11])
      num_fav = int(line[12])

      # update studio and source lookups
      studio, studio_addtl = update_studio(studios, studio)
      update_source(sources, source)

      # then add to dictionary
      anime_dict[animename] = \
          [animenum, year, season, episodes,
              studio, studio_addtl,
              source, score, num_ratings, num_fav]

  anime_studios = sorted(list(studios))
  anime_sources = sorted(list(sources))
  anime_headers = ['Anime ID', 'Season', 'Episodes', 'Studio',
                 'Source', 'Score', '# Ratings', '# Favorites']
  return anime_headers, anime_studios, anime_sources, anime_dict

def get_season(season_year_str):
  season_str, year_str = season_year_str.split(' ')
  season = SEASON_STRS.index(season_str)
  return int(year_str), season

def preprocess_name(anime_str):
  anime_str = ''.join([x.strip() for x in anime_str.split('(TV)')])
  return anime_str

def update_studio(studios, studio):
  studio_list = [x.strip("[] '") for x in studio.split(',')]
  studio = studio_list[0]
  studios.add(studio)
  studio_addtl = ''
  if len(studio_list) > 1:
    studio_addtl = studio_list[1]
    studios.add(studio_addtl)
  return studio, studio_addtl

def update_source(sources, source):
  sources.add(source)

def anime_array(anime_dict, anime_studios, anime_sources):
  studio_dict = dict([(studio, i) for i, studio in enumerate(anime_studios)])
  source_dict = dict([(source, i) for i, source in enumerate(anime_sources)])
  tups = []
  anime_by_id = sorted(list(anime_dict.keys()),
                  key=lambda key: anime_dict[key][ANIME_ID])
  for anime in anime_by_id:
    anime_info = anime_dict[anime]
    studio_ind = studio_dict[anime_info[STUDIO]]
    if anime_info[STUDIO_ADDTL] == '':
      studio_addtl_ind = -1
    else:
      studio_addtl_ind = studio_dict[anime_info[STUDIO_ADDTL]]
    source_ind = source_dict[anime_info[SOURCE]]
    tups.append((anime_info[ANIME_ID],
            anime_info[YEAR], anime_info[SEASON],
            anime_info[EPISODES],
            studio_ind, studio_addtl_ind, source_ind,
            anime_info[SCORE],
            anime_info[NUM_RATINGS],
            anime_info[NUM_FAV]))
  anime_np_lookup = dict(enumerate(anime_by_id))
  return np.array(tups), anime_np_lookup
