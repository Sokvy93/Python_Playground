#Creating dict
dict = {'k1':100, 'k2':'val2', 'k3':2.5}

#Dict and list inside of dict
dict = {'k1':{'key1':22}, 'k2':[1,2,3], 'k3':'python'}

dict['k1']['key1']  #To get the value 22 
dict['k2'][1]  #To get the value 2

dict['k3'] = 200   #To add a key value to dict
dict['k1'] = "NEW VALUE"    #To overwrite an existing key value pair
dict.pop('k3')  #To pop off a key value and you need to define which key you want to pop off of

dict.keys()  #To see keys
dict.values()  #To see the values
dict.items()   #To see the parings together 

