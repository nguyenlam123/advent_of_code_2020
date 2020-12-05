import math
import sys

def partition_at(full_range, index):
  return 2 ** (full_range - index)

def get_seat(file):
  seat_ids = []
  for line in file:
    MAX_EXPONENT = 6
    boarding_pass = line.split('\n')[0]
    rows = [0, 127]
    columns = [0, 7]

    for i,char in enumerate(boarding_pass):
      if char == 'F':
        rows[1] = math.floor(rows[1] - partition_at(MAX_EXPONENT, i))
      elif char == 'B':
        rows[0] = math.ceil(rows[0] + partition_at(MAX_EXPONENT, i))
      elif char == 'R':
        columns[0] = math.ceil(columns[0] + partition_at(len(boarding_pass) - 1, i))
      elif char == 'L':
        columns[1] = math.floor(columns[1] - partition_at(len(boarding_pass) - 1, i))
    
    if rows[0] == rows[1] and columns[0] == columns[1]:
      seat_ids.append(rows[0] * 8 + columns[0])
  return seat_ids

def max_seat_id(seat_ids):
  max = -sys.maxsize - 1
  
  for seat_id in seat_ids:
    if seat_id > max:
      max = seat_id
  
  return max