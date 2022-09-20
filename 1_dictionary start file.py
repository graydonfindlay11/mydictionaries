import random
from site import check_enableusersite

phonebook = {'Chris':'555−1111',        #Chris is the KEY, the number is the VALUE
             'Katie':'555−2222',
             'Joanne':'555−3333'}

#dictionary: object that stores a collection of data
#each element consists of a key and value      KEY MUST BE IMMUTABLE OBJECT 
#to recieve  as specific value, use the key associated with it 

print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(type(phonebook))      
print(phonebook['Chris'])
phone = phonebook['Chris']

print(phone)

mydictionary = {}
print(mydictionary)

mydictionary = dict(m=8, n=9)
print(mydictionary)

print()
print('*****  end section 1 ********')
print()






print()
print('*****  start section 2 - search dictionary ********')
print()


name = 'Drexy'

if name in phonebook:
    print(phonebook[name])
else:
    print(name, "is not in the phonebook")



print()
print('*****  end section 2 ********')
print()






print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)
phonebook['Chris'] = '555-0123'
phonebook['Joe'] = '555-4444'
print(phonebook)



print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

#del phonebook['Chris']   #delete gives u an error if the KEY is not found
#print(phonebook)

print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for k in phonebook:       # the default iteration is the KEYS when using a FOR Loop
    print(k)              # KEY is also just a variable 
    print(phonebook[k])
    
print()

for value in phonebook.values():
    print(value)
print()


for k,v in phonebook.items():
    print("Key: ",k, "  Value: ", v)
print()

for tuple in phonebook.items():
    print(tuple)
print()


print()
print('*****  end section 5 ********')
print()







print()
print('*****  start section 6 - using get and clear ********')  #gives u an option to say a msg instead of an error if not found
print()

phone = phonebook.get('Chris', 'key not found')
print(phone)
print()

#phonebook.clear()            --clears out elements of phonebook but doesnt delete it
#print(phonebook)

print()
print('*****  end section 6 ********')
print()





print()
print('*****  start section 7 - using pop method ********')
print()


#a = phonebook.pop('Chris','not found')     #finds a key and pops out the information from phonebook

#print(a)


print()
print('*****  end section 7 ********')
print()




print()
print('*****  start section 8 - using popitem ********')
print()


#a = phonebook.popitem()      #random part doesnt work, it just pops out the last element

#print(a)



print()
print('*****  end section 8 ********')
print()




print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)
print(list_of_keys)

random_key = random.choice(list_of_keys)
print()
print(random_key)
print()


random_value = phonebook[random_key]
print(random_value)
print()

#Alternatively

random_value = phonebook[random.choice(list(phonebook))]    #this is the same as above code but condensed
print(random_value)


print()
print('*****  end section 9 ********')
print()







