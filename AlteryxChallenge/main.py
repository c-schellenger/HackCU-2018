







dataFile = open("rawdata.txt", 'r')

data = dataFile.read() 
#print(data)

binary = []
while data:
    binary.append(data[:8])
    data = data[8:]

#print(binary)

chars = []
for n in binary:
    chars.append(chr(int(n, 2)))

#print(chars)
str1 = ''.join(str(e) for e in chars)
print(str1)