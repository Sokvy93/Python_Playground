#Creating function

def name_of_function():
  '''
  Docstring explains function.
  '''
  return "Hello"   #use return instead of print since return can be stored as a variable.
  
  
#Simple example

def dog_check(mystring):
  if 'dog' in mystring.lower():
    return True
  else:
    return False
#This is a beginner move. x in y.lower() is already a boolean.

dog_check('Dog ran away')

#Expert move:
def dog_check(mystring):
  return 'dog' in mystring.lower()


# *args
def myfunc(*args):              #instead of myfunc(a,b,c,...) no limit of arguments and it will be treated as tuples.
  return sum(args) * 0.05
  
myfunc(14,10,100)


# **kwargs                       # kwargs returns as a dictionary
def myfunc(**kwargs):
  if 'fruit' in kwargs:
    print('My fruit of choice is {}'.format(kwargs['fruit']))
  else:
    print('I did not find any fruit here')
    
myfunc(fruit='apple')


#Combination
def myfunc(*args, **kwargs):
  print('I would like {} {}'.format(args[0], kwargs['food']))
  
myfunc(10,20,30,fruit='orange',food='eggs',animal='dog')



##BONUS Project
#Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, n/
#and every odd letter is lowercase.

def myfunc(word):

  result = ""
  for index, letter in enumerate(word):
    if index % 2 == 0:
      result += letter.lower()
    else:
      result += letter.upper()
  return result
  
myfunc('VictoriaSok')
