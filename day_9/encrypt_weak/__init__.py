def decypher(preamble, nbr, min_idx, max_idx):
  sum = preamble[min_idx] + preamble[max_idx]
  
  if sum == nbr:
    return True
  elif preamble[min_idx] >= nbr:
    return False
  elif max_idx <= min_idx:
    return False
  elif min_idx >= max_idx:
    return False
  elif sum > nbr:
    max_idx += -1
    return decypher(preamble, nbr, min_idx, max_idx)
  elif sum < nbr:
    min_idx += 1
    return decypher(preamble, nbr, min_idx, max_idx)
  return False

def get_err_val(transmission, nbr_preamble):
  err_val = -1
  idx = 0

  while (idx + nbr_preamble) < len(transmission):
    next = idx + nbr_preamble

    preamble = transmission[idx:next]
    preamble.sort()
    is_xmas = decypher(preamble, transmission[next], 0, len(preamble) - 1)

    if is_xmas == False:
      err_val = transmission[next]
      break

    idx += 1

  return err_val

def get_nbr_idx_tuple(idx_nbr):
  return (idx_nbr[0], idx_nbr[1])

def get_cont_sets(cand_cont_set_sort):
  islands = []
  islands.append([])
  curr_island = 0
  curr_pair = cand_cont_set_sort[0]
  islands[curr_island].append(curr_pair)
  idx = 1

  while idx < len(cand_cont_set_sort):
    next_pair = cand_cont_set_sort[idx]
    
    if curr_pair[0] + 1 != next_pair[0]:
      next_island = []
      next_island.append(next_pair)
      islands.append(next_island)
      curr_island += 1
    else:
      islands[curr_island].append(next_pair)
    
    curr_pair = next_pair
    idx += 1
  
  return islands

def find_sub_set(st, curr_terms, err_val):
  sub_set = []
  wanted_contiguous_set = []

  idx = 0

  while (idx + curr_terms) < len(st):
    wcs = st[idx:idx + curr_terms]
    s = sum(n for _, n in wcs)
    
    if s == err_val:
      wanted_contiguous_set = [x[1] for x in wcs]
      break

    idx += 1
  return wanted_contiguous_set

def find_cont_set(islands, err_val):
  sub_set = []

  for st in islands:
    if len(sub_set) > 0:
      break
    max_terms = len(st)
    curr_terms = 2

    while curr_terms < max_terms:
      sub_set = find_sub_set(st, curr_terms, err_val)
      if len(sub_set) > 0:
        break
      curr_terms += 1
  return sub_set

def get_encoding_err(file, nbr_preamble):
  transmission = []
  err_val = -1

  for line in file:
    nbr = line.split('\n')[0]
    transmission.append(int(nbr))

  err_val = get_err_val(transmission, nbr_preamble)
  idx_nbr_map = map(get_nbr_idx_tuple, enumerate(transmission))
  idx_nbr_list = list(idx_nbr_map)
  idx_nbr_list_sort = sorted(idx_nbr_list, key=lambda x: x[1])
  idx_err_val = [i for i, item in enumerate(idx_nbr_list_sort) if item[1] == err_val]
  cand_cont_set = idx_nbr_list_sort[0:idx_err_val[0]]
  cand_cont_set_sort = sorted(cand_cont_set, key=lambda x: x[0])

  islands = get_cont_sets(cand_cont_set_sort)

  cont_set = find_cont_set(islands, err_val)
  cont_set.sort()
  sum = cont_set[0] + cont_set[len(cont_set) - 1]

  return sum