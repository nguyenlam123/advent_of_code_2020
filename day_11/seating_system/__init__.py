from itertools import product, starmap
from copy import copy, deepcopy

EMPTY = 'L'
FLOOR = '.'
OCCUPIED = '#'

def get_adjacent(x1, y1):
  x, y = (x1, y1)
  cells = starmap(lambda a,b: (x+a, y+b), product((0,-1,+1), (0,-1,+1)))
  neighbours = list(cells)[1:]
  return neighbours

def get_valids(x, init_seat_layout, row_idx):
  return x[0] >= 0 and x[1] >= 0 and x[0] < len(init_seat_layout) and x[1] < len(init_seat_layout[row_idx])

def get_next_matrix(init_seat_layout, cnt_occupied):
  curr_iter_layout = deepcopy(init_seat_layout)

  for i, row in enumerate(init_seat_layout):
    for j, column in enumerate(init_seat_layout[i]):
      neighbours = get_adjacent(i, j)
      valid_neighbours = list(filter(lambda x: get_valids(x, init_seat_layout, i), neighbours))
      nearest_occupied_seats = 0

      for coord in valid_neighbours:
        seat = init_seat_layout[coord[0]][coord[1]]
        if seat == OCCUPIED:
          nearest_occupied_seats += 1
      
      curr_seat = init_seat_layout[i][j]
      if nearest_occupied_seats == 0 and curr_seat == EMPTY:
        curr_iter_layout[i][j] = '#'
        cnt_occupied += 1
      elif nearest_occupied_seats >= 4 and curr_seat == OCCUPIED:
        curr_iter_layout[i][j] = 'L'
        cnt_occupied -= 1
  
  return (curr_iter_layout, cnt_occupied)

def get_occupied_seats(file):
  init_seat_layout = []
  curr_occupied_seats = 0

  for line in file:
    row = list(line.split('\n')[0])
    init_seat_layout.append(row)

  (next, next_occupied) = get_next_matrix(init_seat_layout, 0)
  
  if curr_occupied_seats == next_occupied:
    return curr_occupied_seats

  while curr_occupied_seats != next_occupied:
    curr_iter_mat = next
    curr_occupied_seats = next_occupied
    (next, next_occupied) = get_next_matrix(curr_iter_mat, next_occupied)
    if curr_occupied_seats == next_occupied:
      break

  print('curr_occupied_seats is: ', curr_occupied_seats)

  return curr_occupied_seats