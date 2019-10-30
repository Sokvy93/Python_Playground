x = 100

def func():
  global x 
  print(f'X is {x})
  
  #Local reassignment on a global variable.
  
  x = 'NEW VALUE'
  print(f'I just locally changed global X to {x})
  
  


### Safer and cleaner path ###

x = 100

def func(x):
  
  print(f'X is {x})
  
  #Local reassignment on a global variable.
  
  x = 'NEW VALUE'
  print(f'I just locally changed global X to {x})
  return x
  
  
func(x)
#Then
x = func(x)
print(x)
