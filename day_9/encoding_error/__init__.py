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

def get_encoding_err(file, nbr_preamble):
  transmission = []

  for line in file:
    nbr = line.split('\n')[0]
    transmission.append(int(nbr))
  
  return get_err_val(transmission, nbr_preamble)