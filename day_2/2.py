COUNT = 0

def exactly_one_element_in_common(arr1, arr2):
  count = 0 
  for e1 in arr1:
    for e2 in arr2:
      if e1 == e2:
        count += 1
  return True if count == 1 else False

if __name__ == '__main__': 
  file = open('advent_of_code_day_2/day2.txt', 'r')
  
  for line in file:
    poll_pass = line.split()
    range = poll_pass[0]
    positions = [int(char) for char in range.split('-') if char.isdigit()]
    poll_char = poll_pass[1].split(':')[0]
    
    password = poll_pass[2]
    matches = []
    for i,p in enumerate(password):
      if p == poll_char:
        matches.append(i + 1)
    if exactly_one_element_in_common(matches, positions):
      COUNT += 1
  print(COUNT)