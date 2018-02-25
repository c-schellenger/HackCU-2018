import string
inputFile = open('decrptedout.txt', 'r')

data = inputFile.read()
all=string.maketrans('','')
nodigs=all.translate(all, string.digits)
tmp = data.translate(all, nodigs)


values = []

while tmp:
    values.append(tmp[:2])
    tmp = tmp[2:]

chars = []
for n in values:
    chars.append(chr(int(n)))

print(chars)
