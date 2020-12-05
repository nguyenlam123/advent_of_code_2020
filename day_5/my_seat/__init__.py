from boarding_pass import get_seat

def find_my_seat(file):
  my_seat = -1
  seats = get_seat(file)
  seats.sort()
  for i,seat in enumerate(seats):
    diff = seat - i
    if diff == seats[0] + 1:
      my_seat = seat - 1
      break
  return my_seat
