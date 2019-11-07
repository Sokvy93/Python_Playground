### 007 Game ###
#If there is 007 in such array, return True

def spy_game(nums):

  code = [0,0,7,'x']
  
  for i in nums:
    if num == code[0]:
      code.pop(0)
      
  return len(code) == 1


#----------------------------------------------------


##Medtronic interview question

#Q. Given a string write a fuction, determine, that determines its encapsulazation.

#eg
#determine ("[a b 0 0 7 6 8]")---> True
#determine ("{haha]")---> False
#determine ("(ha[ok999])")---> True
#determine ("{[ ]}")---> True
#determine ("{[ }]")---> False

def enclosed(str):
  stackArr = ['dummy']
  for char in str:
    if char == '[' :
      stackArr.append(']')
    elif char == '(' :
      stackArr.append(')')
    elif char == '{' :
      stackArr.append('}')
    elif char == ')' or char == ']' or char == '}' :
      if stackArr[-1] == char:      #arr[-1] will return the very last element
        stackArr.pop()
      else:
        return 'not enclosed'
