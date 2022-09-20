person = {}                                 #dictionaries can be mixed and matched and have different elements
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print()
print(person)
print()

print(person['children'][1])
print()


print(person['pets']['cat'])
print()
print()

for kid in person['children']:
    print(kid)
print()

for pet in person['pets']:
    print(person['pets'][pet])