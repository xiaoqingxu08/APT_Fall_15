# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to 
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
  # Returned string pair should be ordered by dictionary order
  # I.e., if the highest affinity pair is "foo" and "bar"
  # return ("bar", "foo").
  site_user_dict = dict() 
  site_cnt = len(site_list)
  for index in xrange(site_cnt):
    if site_list[index] in site_user_dict: 
      pass  
    else:
      site_user_dict[site_list[index]] = set()
    site_user_dict[site_list[index]].add(user_list[index])

  max_affinity = 0
  max_pair = ('','')
  for site_a in site_user_dict:
    for site_b in site_user_dict:
      if site_a == site_b: continue
      affinity = 0
      for elem in site_user_dict[site_a]:
        if elem in site_user_dict[site_b]: affinity += 1
      if affinity > max_affinity:
        max_affinity = affinity
        if site_a <= site_b: max_pair=(site_a, site_b)
        else: max_pair = (site_b, site_a)
    
  return max_pair
