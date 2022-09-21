infile = open("info_security.txt", "r")

for line in infile:
    text = line

code = {"A" : "L", "B" : "S", "C" : ">", "D" : "9", "E" : "M", "F" : "]", "G" : "1", "H" : "&", "I" : "=",
        "J" : "<", "K" : "|", "L" : "2", "M" : "_", "N" : "Z", "O" : "3", "P" : "V", "Q" : ":", "R" : "5", 
        "S" : "T", "T": "8", "U" : ".", "V" : "W", "X" : "P", "Y" : "^", "Z" : "4"
        } 


new_code = ""

for x in range(len(text)):
    if text[x] in code.keys():
        new_code += code[text[x]]
    else:
        new_code += text[x]

print(new_code)
outfile = open("encrypted.txt", "w")
outfile.write(new_code + '\n')



outfile.close()
