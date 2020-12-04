REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
COUNT = 0
ELEMENTS = 0

if __name__ == '__main__':
  file = open('day_4/day4.txt', 'r')

  passports = []
  temp_fields_dict = {}
  for i,line in enumerate(file):
    if line != '\n':
      fields = line.split('\n')[0].split(' ')
      for field in fields:
        key_val = field.split(':')
        temp_fields_dict[key_val[0]] = key_val[1]
    
    if line == '\n':
      ELEMENTS += 1
      field_keys = temp_fields_dict.keys()
      if set(REQUIRED_FIELDS).issubset(set(field_keys)) or field_keys == REQUIRED_FIELDS:
        COUNT += 1
      temp_fields_dict = {}
  
  if len(temp_fields_dict.keys()) > 0:
    field_keys = temp_fields_dict.keys()
    if set(REQUIRED_FIELDS).issubset(set(field_keys)) or field_keys == REQUIRED_FIELDS:
      COUNT += 1
    temp_fields_dict = {}

  print(COUNT)
  print(ELEMENTS)
  print('hello')
