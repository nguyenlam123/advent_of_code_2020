def is_diff(d1, d2, diff):
  return (d1 - d2) == diff

def calc_mul_jolt_diff(file):
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

  return cnt_one_jolt * cnt_three_jolt