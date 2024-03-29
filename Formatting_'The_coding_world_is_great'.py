print('The {} {} {} {}'.format('world', 'great', 'coding', 'is')

print('The {2} {0} {3} {1}'.format('world', 'great', 'coding', 'is')

print('The {c} {w} {i} {g}'.format(w='world', g='great', c='coding', i='is')


#BONUS
#Float Formatting 
#{value:width.precision f}

result = 222/2323
print("The result was {r:1.3f}".format(r=result))

#F Strings
name = Tori 
print(f'Hello, my name is {name}')   #Instead of print('Hello, my name is {}'.format(name))


##For loops and formating

index_count = 0 

for letter in 'abcde':
  print('At index {} the letter is {}'.format(index_count, letter))
  index_count += 1
  
#Enumerable function
word = 'abcde'

for index,letter in enumerate(word):
  print(index)
  print(letter)
  print('\n')
