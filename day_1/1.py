RES = 2020

if __name__ == '__main__': 
  file = open('advent-of-code-1.txt', 'r')
  
  numbers = []
  for line in file:
    numbers.append(int(line))
  
  numbers.sort()
  min_idx = 0
  max_idx = len(numbers) - 1
  while min_idx < max_idx:
    first_term = numbers[min_idx]
    second_term = numbers[max_idx]
    sum = first_term + second_term
    
    if sum < RES:
      min_idx = min_idx + 1
    elif sum > RES:
      max_idx = max_idx - 1
    else:
      break
  
  if sum == RES:
    print(numbers[min_idx] * numbers[max_idx])