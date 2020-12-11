def count_gold(bag, deps, dict_in_dict, bags, shiny_gold_list):
  if len(bags) == 0:
    return 0
  elif type(deps) is not dict:
    bags.discard(bag)
    return 0
  # Grandchild of bag is shiny gold, but child of bag has already been removed
  elif any(item in shiny_gold_list for item in list(deps.keys())) and bag in bags:
    shiny_gold_list.append(bag)
    bags.discard(bag)
    return 1
  elif type(deps) is dict and bag in bags:
    if 'shinygold' in deps and deps != dict_in_dict:
      shiny_gold_list.append(bag)
      bags.discard(bag)
      return 1
    else:
      sum = 0
      for d in deps:
        if d in dict_in_dict:
          temp = count_gold(d, dict_in_dict[d], dict_in_dict, bags, shiny_gold_list)
          sum += temp
        bags.discard(d)
      if sum > 0 and bag not in deps:
        # Count parent as well
        shiny_gold_list.append(bag)
        bags.discard(bag)
        sum += 1
      return sum
  else:
    bags.discard(bag)
    return 0
  

def get_gold(dict_in_dict, bags, shiny_gold_list):
  sum = 0
  
  for bag, dctnr in dict_in_dict.items():
    gold_count = count_gold(bag, dctnr, dict_in_dict, bags, shiny_gold_list)
    sum += gold_count
  return sum
  

def remove_deps(dep, dict_in_dict):
  if dep in dict_in_dict:
    sub_dict = dict_in_dict[dep]
    if type(sub_dict) is dict:
      for key in sub_dict:
        remove_deps(key, dict_in_dict)
      del dict_in_dict[dep]
    else:
      del dict_in_dict[dep]

def remove_shiny_gold_assoc(dict_in_dict):
  did = dict(dict_in_dict)
  for key, dctnr in dict_in_dict.items():
    if key == 'shinygold':
      if type(dctnr) is dict:
        for dep in dctnr:
          remove_deps(dep, did)
      del did[key]
  return did

def remove_leaf_bags(d):
  cpy = dict(d)
  for key, value in d.items():
    if value == 0:
      del cpy[key]
  return cpy


def get_shiny_gold_containers(file):
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
  cpy_container = remove_shiny_gold_assoc(containers)
  cpy_container2 = remove_leaf_bags(cpy_container)
  keys_to_iterate = set(cpy_container.keys())
  golds = []

  shiny_gold_containers = get_gold(cpy_container2, keys_to_iterate, golds)
    
  return shiny_gold_containers