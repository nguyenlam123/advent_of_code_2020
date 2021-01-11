def get_acc_val(file):
  instructions = []

  for line in file:
    op_arg = line.split('\n')[0].split(' ')
    instruction = (op_arg[0], op_arg[1])
    instructions.append(instruction)
  
  acc_val = 0
  visited_instructions = set()
  curr_len = 0
  op = instructions[0][0]
  arg = instructions[0][1]
  idx = 0
  while len(visited_instructions) < len(instructions):
    visited_instructions.add(idx)
    curr_len += 1
    if len(visited_instructions) != curr_len:
      break
    if op == 'acc':
      acc_val += int(arg)
      idx += 1
    elif op == 'jmp':
      idx += int(arg)
    else:
      idx += 1
    op = instructions[idx][0]
    arg = instructions[idx][1]

  return acc_val