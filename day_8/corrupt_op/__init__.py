def run_boot_code(instructions):
  acc_val = 0
  visited_instructions = set()
  curr_len = 0
  op = instructions[0][0]
  arg = instructions[0][1]
  idx = 0
  jmps_nops = set()
  is_terminated = True

  while len(visited_instructions) < len(instructions):
    visited_instructions.add(idx)
    curr_len += 1
    
    if len(visited_instructions) != curr_len:
      is_terminated = False
      break
    if op == 'acc':
      acc_val += int(arg)
      idx += 1
    elif op == 'jmp':
      jmps_nops.add((op, arg, idx))
      idx += int(arg)
    else:
      jmps_nops.add((op, arg, idx))
      idx += 1
    
    if idx == len(instructions):
      is_terminated = True
      break

    op = instructions[idx][0]
    arg = instructions[idx][1]

  return (acc_val, jmps_nops, is_terminated)

def get_acc_val(file):
  instructions = []
  acc_val = 0

  for line in file:
    op_arg = line.split('\n')[0].split(' ')
    instruction = (op_arg[0], op_arg[1])
    instructions.append(instruction)

  jmps_nops = run_boot_code(instructions)[1]
  for instr in jmps_nops:
    op, arg, idx = instr
    cpy_instructions = []
    for instruction in instructions:
      cpy_instructions.append(list(instruction))

    if op == 'jmp':
      cpy_instructions[idx][0] = 'nop'
    else:
      cpy_instructions[idx][0] = 'jmp'
    
    acc, corrupted_ops, is_terminated = run_boot_code(cpy_instructions)
    if is_terminated == True:
      acc_val = acc
      break
  
  return acc_val