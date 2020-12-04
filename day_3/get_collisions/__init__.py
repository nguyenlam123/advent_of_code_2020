def get_collisions(file, right, down):
  COUNT_TREES = 0
  OPEN = '.'
  TREE = '#'
  PATTERN_TIMES = 500

  matrix = []
  for line in file:
    chars = list(line.split('\n')[0])
    row = []
    for i in range(PATTERN_TIMES):
      row = row + chars
    matrix.append(row)
  
  i = down
  j = right
  while i < len(matrix) and j < len(matrix[0]):
    loc = matrix[i][j]

    if loc == TREE:
      COUNT_TREES += 1

    i += down
    j += right
  return COUNT_TREES