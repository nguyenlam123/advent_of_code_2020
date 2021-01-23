import itertools
import math

def is_diff(d1, d2, diff):
  return (d1 - d2) == diff

def is_up_to(d1, d2, diff):
  return (d1 - d2) < diff

def is_max_diff(d1, d2, diff):
  return (d1 - d2) <= diff

def is_eq_or_exceeds(d1, d2, diff):
  return (d1 - d2) >= diff

def is_valid_sub_conn(adapters, meta):
  if meta['prev'] == -1 and meta['min'] != adapters[0]:
    return False
  elif meta['next'] == -1 and meta['max'] != adapters[-1]:
    return False

  idx = 1
  curr_adapter = adapters[0]
  is_valid = True
  while idx < len(adapters):
    next_adapter = adapters[idx]

    if is_max_diff(next_adapter, curr_adapter, 3) == False:
      is_valid = False
      break
  
    curr_adapter = next_adapter
    idx += 1
  return is_valid

def is_valid_conn(adapters, device):
  if adapters[0] != 0:
    return False
  
  if adapters[-1] != device:
    return False
  
  idx = 1
  curr_adapter = adapters[0]
  is_valid = True
  while idx < len(adapters):
    next_adapter = adapters[idx]

    if is_max_diff(next_adapter, curr_adapter, 3) == False:
      is_valid = False
      break
  
    curr_adapter = next_adapter
    idx += 1
  return is_valid

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

def get_combs(all_combs, meta, device):
  combs = []
  for comb in all_combs:
    list_comb = list(comb)
    if len(list_comb) > 0:
      list_comb.sort()

      if meta['prev'] != -1:
        list_comb.insert(0, meta['prev'])
      
      if meta['next'] != -1:
        list_comb.append(meta['next'])

      if is_valid_sub_conn(list_comb, meta):
        combs.append(list_comb)
  return combs
          
def get_nbr_dis_conn(file):
  adapters = []
  cnt_one_jolt = 0
  cnt_three_jolt = 0

  for line in file:
    nbr = line.split('\n')[0]
    adapters.append(int(nbr))
  
  adapters.sort()

  idx = 1
  curr_adapter = adapters[0]

  # outlet
  if is_diff(adapters[0], 0, 1):
    cnt_one_jolt += 1
  elif is_diff(adapters[0], 0, 3):
    cnt_three_jolt += 1

  while idx < len(adapters):
    next_adapter = adapters[idx]
    diff = next_adapter - curr_adapter
    
    if is_diff(next_adapter, curr_adapter, 1):
      cnt_one_jolt += 1
    elif is_diff(next_adapter, curr_adapter, 3):
      cnt_three_jolt += 1

    curr_adapter = next_adapter
    idx += 1

  # device
  last = adapters[len(adapters) - 1]
  device = last + 3
  if is_diff(device, last, 1):
    cnt_one_jolt += 1
  elif is_diff(device, last, 3):
    cnt_three_jolt += 1

  adapters.insert(0, 0)
  adapters.append(device)

  start = 0
  outlet = 0
  alternatives = set()
  degrees_of_freedom_nbr = set()
  combs = 1
  min = 0

  while start < len(adapters):
    curr_adapter = adapters[start]
    alt = start + 1

    while alt < len(adapters):
      if is_max_diff(adapters[alt], adapters[start], 3):
        alternatives.add(curr_adapter)
        alternatives.add(adapters[alt])
        alt += 1
      else:
        all_curr_comb = list(powerset(alternatives))
        sorted_alternatives = list(alternatives)
        sorted_alternatives.sort()
        meta = {
          'min': sorted_alternatives[0],
          'max': sorted_alternatives[len(sorted_alternatives) - 1]
        }
        if outlet in alternatives:
          meta['prev'] = -1
          meta['next'] = adapters[adapters.index(meta['max']) + 1]
        elif device in alternatives:
          meta['prev'] = adapters[adapters.index(meta['min']) - 1]
          meta['next'] = -1
        else:
          meta['prev'] = adapters[adapters.index(meta['min']) - 1]
          meta['next'] = adapters[adapters.index(meta['max']) + 1]
        
        curr_comb = get_combs(all_curr_comb, meta, device)
        combs *= len(curr_comb)

        alternatives = set()
        break
    start = alt
          
    # if len(alternatives) >= 2:
    #   sub = alternatives[0:len(alternatives) - 1]
    #   degrees_of_freedom_nbr.update(sub)
  return combs