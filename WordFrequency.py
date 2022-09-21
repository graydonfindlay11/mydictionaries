infile = open("sometext.txt", "r")

words_listed = {}

x = 0

texts = infile.read()

texts = texts.rstrip('\n' + ',' + '.')
list = texts.split(" ")

print(list)

for name in list:
    if name in list and name not in words_listed:
        i = list.count(name)
        words_listed[name] = {'count': i}


print (words_listed["the"]["count"])

