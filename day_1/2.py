RES = 2020

if __name__ == '__main__': 
  file = open('advent-of-code-1.txt', 'r')
  
  numbers = []
  for line in file:
    numbers.append(int(line))
  
  numbers.sort()
  
  max_idx = len(numbers) - 1
  for i,number in enumerate(numbers):
    mid_idx = i + 1
    max_idx = len(numbers) - 1
    while mid_idx < max_idx:
      sum = number + numbers[mid_idx] + numbers[max_idx]

      if sum == RES:
        min_idx = numbers.index(number)
        print(numbers[min_idx] * numbers[mid_idx] * numbers[max_idx])
        break
      elif sum < RES:
        mid_idx = mid_idx + 1
      else:
        max_idx = max_idx - 1
