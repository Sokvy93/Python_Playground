### MAP Function ###

#With Numbers

def square(num):
  return num**2
  
nums_list = [1,2,3,4,5,6]

for i in map(square, nums_list):
  print(i)
  
  
#Other way, to get the list back

list(map(square,nums_list))



#With String 

def slicer(mystring):
  if len(mystring)%2 == 0:
    return 'EVEN'
  else:
    return mystring[0]

names = ['Tori', 'David', 'Ann', 'Jesus']

lsit(map(slicer,names))


### Filter Function ###

#NOTE: Filter by a function that returns either True or False

def check_even(num):
  return num%2 == 0
  
list_nums = [1,2,3,4,5,6,7,8]

list(filter(check_even,list_nums))
#or
for n in filter(check_even,list_nums)
  print(n)
  
  

### Lambda Expression ###

#It is known as an anonymous function 

lambda num: num ** 2          #This is equal to 
                              #def square(num):
                                #return num ** 2
list(map(lambda num: num ** 2, list_nums))

list(filter(lambda num: num % 2 == 0, list_nums))

list(map(lambda name: name[0], names))

##NOTE: Only uselambda expression for something that can be easily coded
