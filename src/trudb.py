#!/usr/bin/env python

import os
import subprocess
import sys
import csv
from pathlib import Path

# Output path and filename
result_dir = Path("result")
gamedb_file = Path(result_dir, "gameDB.csv")
game_list = Path(result_dir, "my_games.txt")
# Path to galaxy_library_export script
gog_script = Path("import", "GOG-Galaxy-Export-Script", "galaxy_library_export.py")
# String variable to contain all game names
my_games = ""

# Create the output dir if needed
if result_dir.is_file():
   os.remove(result_dir)
if not result_dir.is_dir():
   os.mkdir(result_dir)

# Run galaxy_library_export script
subprocess.check_call([sys.executable, gog_script, "-o", gamedb_file])

# Open game database csv file
with open(gamedb_file, 'r', encoding='utf-8') as csv_file:
   reader = csv.reader(csv_file)
   # Index for the game
   i = 0
   # The name of the game is on the first part of the row
   for row in reader:
      row_string = ' '.join([str(elem) for elem in row])
      name = row[0].split('\t')
      # Store game name in string var
      if i > 0:
         my_games += name[0] + "\n"
      i += 1
csv_file.close()

# Write the string to file
with open(game_list, 'w', encoding='utf-8') as games_file:
    games_file.write(my_games)
games_file.close()
