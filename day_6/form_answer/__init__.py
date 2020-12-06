def get_form_answers(file):
  count = 0
  answers = []
  unique_answers = []

  for line in file:
    if line != '\n':
      form = line.split('\n')[0].split(' ')[0]
      for answer in form:
       answers.append(answer)
    else: 
      unique_answers = set(answers)
      count += len(unique_answers)
      unique_answers = []
      answers = []
  
  if len(answers) > 0:
    unique_answers = set(answers)
    count += len(unique_answers)
    unique_answers = []
  
  return count