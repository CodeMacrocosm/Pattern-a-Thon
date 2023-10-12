import random

size=71 
n_print=1

while(n_print<=size):
  for i in range(int((size-n_print)/2)):
    print(" ", end='')
  for i in range(n_print):
    if(i==0 or i==(n_print-1)):
      print("*", end='')
    else:
      if(random.randint(0,15)==5):
        print("@", end='') #Put a decoration on the tree
      else:
        print("*", end='')
  n_print=n_print+2
  print()

trunk_size=int(size/5)

for j in range(int(trunk_size/2)):
  for i in range(trunk_size*2):
      print(" ", end='')
  for i in range(trunk_size):
      print("I", end='')
  print()
