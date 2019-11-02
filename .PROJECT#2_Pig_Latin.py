#Creating Pig Latin game

def pig_latin(word):
  first_letter = word[0]
  
  #Check if vowel
  if first_letter in 'aeiou':
    pig_word = word + 'ay'
  else:
    pig_word = word[1:] + first_letter + 'ay'
    
  return pig_word

pig_latin('word')
