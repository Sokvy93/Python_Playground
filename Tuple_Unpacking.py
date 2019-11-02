##Unpacking tuple
mylist = [(1,2),(3,4),(5,6),(7,8),(9,10)]

for a,b in mylist:
  print(b)   #or a. 
 
 
##Unpacking dict
d = {'k1':1, 'k2':2, 'k3':3}
for key,value in d.items():          #If you only put d, it will only show keys.
  print(value)
  
#If you only want values
for value in d.values():
  print(value)
