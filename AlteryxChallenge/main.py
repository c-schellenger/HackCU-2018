import pandas as pd
import urllib.request, json

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
#print(cleaned_data)

d = {'url' : cleaned_data[0::3], 'query' : cleaned_data[1::3], 'value' : cleaned_data[2::3]}

df = pd.DataFrame(d)
#print(df)

decrypted = []
outFile = open('decrptedout.txt','w')
#"""
for index, row in df.iterrows():
    url = row['url']
    print("Retrieving from", url)
    querytmp = row['query']
    print(querytmp)
    query = row['query'].split(".")
    print("query:", query)
    value = row['value']
    #print(url)
    #print(query)
    with urllib.request.urlopen(url) as url:
        jsondata = json.loads(url.read().decode())
        """query_result = jsondata[query[0]]
        query.pop(0)
        #print(query_result)
        print(query)"""
        query_result = jsondata
        if query[0] == "6r9a-dfdj":
            decrypted.append(query[0])
        elif querytmp =="columns.0.cachedContents.top.6.count":
            decrypted.append("")
        elif querytmp =="columns.0.cachedContents.top.19.count":
            decrypted.append("")

        else:
            while query:
                try:
                    query_result = query_result[query[0]]
                except TypeError:
                    query_result = query_result[int(query[0])]
                query.pop(0)
                #print(query_result)
            #print("result string:", query_result)
            #print("value:", value)
            decrypted.append(query_result)
            outFile.write(str(query_result))
            #print("decrypted char:", str(query_result)[int(value)])
print(decrypted)

outFile.close()
"""
with urllib.request.urlopen("https://data.cityofnewyork.us/api/views/kku6-nxdu") as url:
        jsondata = json.loads(url.read().decode())
        print(jsondata)
        print(jsondata["columns"])
        print(jsondata["columns"]["0"])
        print(jsondata["columns"][0]["cachedContents"])
        print(jsondata["columns"][0]["cachedContents"]["top"])
        print(jsondata["columns"][0]["cachedContents"]["top"][16])
        print(jsondata["columns"][0]["cachedContents"]["top"][16]["count"])
"""
