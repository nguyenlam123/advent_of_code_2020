def get_form_answers_intersect(file):
  count_humans = 0
  count_everyone = 0
  answers_dict = {}

  for line in file:
    if line != '\n':
      form = line.split('\n')[0].split(' ')[0]
      for answer in form:
        if answer in answers_dict:
          answers_dict[answer] += 1
        else:
          answers_dict[answer] = 1
      count_humans += 1
    else: 
      for answer, cnt in answers_dict.items():
        if cnt == count_humans:
          count_everyone += 1
      count_humans = 0
      answers_dict = {}
  
  if len(answers_dict.keys()) > 0:
    for answer, cnt in answers_dict.items():
      if cnt == count_humans:
        count_everyone += 1
    count_humans = 0
    answers_dict = {}
  
  return count_everyone