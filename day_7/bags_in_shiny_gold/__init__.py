def remove_deps(dep, amount, dict_in_dict, golds):
  if dep in dict_in_dict:
    sub_dict = dict_in_dict[dep]
    if type(sub_dict) is dict:
      sum = 0
      for key, value in sub_dict.items():
        sum += value * remove_deps(key, value, dict_in_dict, golds)
      golds[dep] = sub_dict
      return sum
    else:
      golds[dep] = 0
      return 1

def remove_shiny_gold_assoc(dict_in_dict):
  golds = {}
  sum = 0
  shiny_gold = {}
  did = dict(dict_in_dict)
  for key, dctnr in dict_in_dict.items():
    if key == 'shinygold':
      if type(dctnr) is dict:
        shiny_gold = dctnr
        for dep, amount in dctnr.items():
          sum += amount + amount * remove_deps(dep, amount, dict_in_dict, golds)
      del did[key]
  return (golds, sum, shiny_gold)

def get_descendant_bags(bag_type, map):
  if bag_type in map:
    sub_dict = map[bag_type]
    if type(sub_dict) is dict:
      sum = 0
      for key, value in sub_dict.items():
        sum += value + value * get_descendant_bags(key, map)
      return sum
    else:
      return 0

def get_bags(map, shiny_gold):
  sum = 0
  for bag_type, amount in shiny_gold.items():
    sum += amount + amount * get_descendant_bags(bag_type, map)
  return sum

def count_bags_in_shiny_gold(file):
  NO_BAGS = 'no other bags'
  containers = {}

  for line in file:
    container_contents = line.split('contain ')
    container = "".join(container_contents[0].split()).split('bags')[0]
    contents = container_contents[1].split('.')[0].split(', ')

    if contents[0] == NO_BAGS:
      containers[container] = 0
    else:
      bags = {}
      for content in contents: 
        amount = [int(char) for char in content.split() if char.isdigit()]
        bag = ""
        if amount[0] == 1:
          bag = "".join(content.split(str(amount[0]) + ' ')[1].split()).split('bag')[0]
        else:
          bag = "".join(content.split(str(amount[0]) + ' ')[1].split()).split('bags')[0]
        bags[bag] = amount[0]
    
      containers[container] = bags
  bags_map = {}
  golds = remove_shiny_gold_assoc(containers)

  nbr_bags = get_bags(golds[0], golds[2])
    
  return nbr_bags
