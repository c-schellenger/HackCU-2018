import pandas as pd







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
    if chr(int(n, 2)) == '\x9e':
        chars.append(':')
    else:
        chars.append(chr(int(n, 2)))

#print(chars)
str1 = ''.join(str(e) for e in chars)
#print(str1)

cleaned_data = str1.split(',')
print(cleaned_data)


"""df1 = pd.read_json("https://data.cityofnewyork.us/api/views/kku6-nxdu")
print(df1)"""