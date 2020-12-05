import re

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
REQ = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
REQ.sort()

def is_valid_byr(value):
  match_four_digits = re.fullmatch(r"[0-9]{4}", value)
  if match_four_digits:
    return True if int(value) >= 1920 and int(value) <= 2002 else False
  else:
    return False

def is_valid_iyr(value):
  match_four_digits = re.fullmatch(r"[0-9]{4}", value)
  if match_four_digits:
    return True if int(value) >= 2010 and int(value) <= 2020 else False
  else:
    return False

def is_valid_eyr(value):
  match_four_digits = re.fullmatch(r"[0-9]{4}", value)
  if match_four_digits:
    return True if int(value) >= 2020 and int(value) <= 2030 else False
  else:
    return False

def is_valid_hgt(value):
  match = re.fullmatch(r"([0-9]{2,3})(cm|in){1}", value)
  if match:
    height = match.groups()
    if height[1] == 'in':
      return True if int(height[0]) >= 59 and int(height[0]) <= 76 else False
    elif height[1] == 'cm':
      return True if int(height[0]) >= 150 and int(height[0]) <= 193 else False
  else:
    return False

def is_valid_hcl(value):
  match_hair_color = re.fullmatch(r"#([0-9a-f]{6})", value)
  if match_hair_color:
    return True
  else:
    return False

def is_valid_ecl(value):
  match_eye_color = re.fullmatch(r"(amb|blu|brn|gry|grn|hzl|oth){1}", value)
  if match_eye_color:
    return True
  else:
    return False

def is_valid_pid(value):
  match_pass_id = re.fullmatch(r"[0-9]{9}", value)
  if match_pass_id:
    return True
  else:
    return False

def have_fields(keys):
  fields = list(keys)

  if 'cid' in fields:
    fields.remove('cid')
  
  fields.sort()
  return True if fields == REQ else False


def is_valid(fields):
  global REQUIRED_FIELDS

  valids = []
  for field, value in fields.items():
    if field == REQUIRED_FIELDS[0]:
      if is_valid_byr(value):
        valids.append(field)
    elif field == REQUIRED_FIELDS[1]:
      if is_valid_iyr(value):
        valids.append(field)
    elif field == REQUIRED_FIELDS[2]:
      if is_valid_eyr(value):
        valids.append(field)
    elif field == REQUIRED_FIELDS[3]:
      if is_valid_hgt(value):
        valids.append(field)
    elif field == REQUIRED_FIELDS[4]:
      if is_valid_hcl(value):
        valids.append(field)
    elif field == REQUIRED_FIELDS[5]:
      if is_valid_ecl(value):
        valids.append(field)
    elif field == REQUIRED_FIELDS[6]:
      if is_valid_pid(value):
        valids.append(field)

  valids.sort()
  return valids == REQ


def get_pass(file):
  global REQUIRED_FIELDS
  count = 0
  count_new_line = 0

  temp_fields_dict = {}
  for line in file:
    if line != '\n':
      fields = line.split('\n')[0].split(' ')
      for field in fields:
        key_val = field.split(':')
        temp_fields_dict[key_val[0]] = key_val[1]
    else:
      count_new_line += 1
      field_keys = temp_fields_dict.keys() 
      if have_fields(field_keys) and is_valid(temp_fields_dict):
        count += 1
      temp_fields_dict = {}
  
  if len(temp_fields_dict.keys()) > 0:
    field_keys = temp_fields_dict.keys()
    if have_fields(field_keys) and is_valid(temp_fields_dict):
      count += 1
    temp_fields_dict = {}

  return count
