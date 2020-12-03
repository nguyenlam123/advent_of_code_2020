STEPS_RIGHT = 1
STEPS_DOWN = 2
COUNT_TREES = 0
OPEN = '.'
TREE = '#'
PATTERN_TIMES = 500

if __name__ == '__main__':
  file = open('day_3/day3.txt', 'r')

  matrix = []
  for line in file:
    chars = list(line.split('\n')[0])
    row = []
    for i in range(PATTERN_TIMES):
      row = row + chars
    matrix.append(row)
  
  i = STEPS_DOWN
  j = STEPS_RIGHT
  while i < len(matrix) and j < len(matrix[0]):
    loc = matrix[i][j]

    if loc == TREE:
      COUNT_TREES += 1

    i += STEPS_DOWN
    j += STEPS_RIGHT
  print(COUNT_TREES)