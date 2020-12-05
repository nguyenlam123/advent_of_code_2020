REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
REQ = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
REQ.sort()

def have_fields(keys):
  fields = list(keys)

  if 'cid' in fields:
    fields.remove('cid')
  
  fields.sort()
  return True if fields == REQ else False

def get_valid_passports(file):
  required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  count = 0

  passports = []
  temp_fields_dict = {}
  for line in file:
    if line != '\n':
      fields = line.split('\n')[0].split(' ')
      for field in fields:
        key_val = field.split(':')
        temp_fields_dict[key_val[0]] = key_val[1]
    else: 
      field_keys = temp_fields_dict.keys()
      if have_fields(field_keys):
        count += 1
      temp_fields_dict = {}
  
  if len(temp_fields_dict.keys()) > 0:
    field_keys = temp_fields_dict.keys()
    if have_fields(field_keys):
      count += 1
    temp_fields_dict = {}
  
  return count