from itertools import product, starmap
from copy import copy, deepcopy

EMPTY = 'L'
FLOOR = '.'
OCCUPIED = '#'

def get_adjacent(x1, y1, dist):
  x, y = (x1, y1)
  cells = starmap(lambda a,b: (x+a, y+b), product((0, -dist, dist), (0, -dist, dist)))
  neighbours = list(cells)[1:]
  return neighbours

def get_valids(x, init_seat_layout, row_idx):
  return x[0] >= 0 and x[1] >= 0 and x[0] < len(init_seat_layout) and x[1] < len(init_seat_layout[row_idx])

def is_same_diag(coord1, coord2):
  (x1, y1) = coord1
  (x2, y2) = coord2
  return abs(y1 - y2) == abs(x1 - x2)

def is_same_side(y, y1, org):
  diff1 = y1 - org
  diff2 = y - org
  if diff1 > 0 and diff2 > 0:
    return True
  elif diff1 < 0 and diff2 < 0:
    return True
  return False

def in_direction(seat, firsts, current):
  is_same_direction = False
  if len(firsts) == 0:
    return False

  (x, y) = seat
  if is_same_diag(seat, current):
    for coord in firsts:
      (x1, y1) = coord
      if is_same_diag(seat, coord) and is_same_side(y, y1, current[1]) and is_same_side(x, x1, current[0]):
        is_same_direction = True
    return is_same_direction
  
  for coord in firsts:
    (x1, y1) = coord
    if x == x1 and is_same_side(y, y1, current[1]):
      is_same_direction = True
    elif y == y1 and is_same_side(x, x1, current[0]): 
      is_same_direction = True
  return is_same_direction
  

def get_next_matrix(init_seat_layout, cnt_occupied):
  curr_iter_layout = deepcopy(init_seat_layout)

  for i, row in enumerate(init_seat_layout):
    for j, column in enumerate(init_seat_layout[i]):
      dim = max(len(init_seat_layout), len(init_seat_layout[i]))
      nearest_occupied_seats = 0
      firsts = []
      max_valid_neigbours = -1
      for k in range(1, dim + 1):
        neighbours = get_adjacent(i, j, k)
        valid_neighbours = list(filter(lambda x: get_valids(x, init_seat_layout, i), neighbours))
        if len(valid_neighbours) > max_valid_neigbours:
          max_valid_neigbours = len(valid_neighbours)

        for coord in valid_neighbours:
          seat = init_seat_layout[coord[0]][coord[1]]
          current = (i, j)
          if seat == OCCUPIED and in_direction(coord, firsts, current) == False:
            nearest_occupied_seats += 1
            firsts.append(coord)
          elif seat == EMPTY and in_direction(coord, firsts, current) == False:
            firsts.append(coord)
        if len(firsts) == max_valid_neigbours:
          break
      
      curr_seat = init_seat_layout[i][j]
      if nearest_occupied_seats == 0 and curr_seat == EMPTY:
        curr_iter_layout[i][j] = '#'
        cnt_occupied += 1
      elif nearest_occupied_seats >= 5 and curr_seat == OCCUPIED:
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