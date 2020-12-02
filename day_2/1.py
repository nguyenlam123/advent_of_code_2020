COUNT = 0

if __name__ == '__main__': 
  file = open('day2.txt', 'r')
  
  for line in file:
    poll_pass = line.split()
    range = poll_pass[0]
    min_max = [int(char) for char in range.split('-') if char.isdigit()]
    poll_char = poll_pass[1].split(':')[0]
    
    password = poll_pass[2]
    count_match = 0
    for p in password:
      if p == poll_char:
        count_match += 1
    if count_match >= min_max[0] and count_match <= min_max[1]:
      COUNT += 1
  print(COUNT)