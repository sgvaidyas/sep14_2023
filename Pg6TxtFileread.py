fp = open('C:/Users/Administrator/Desktop/myfile1.txt','r')
content = fp.readlines()
print(content)
for line in content:
    linenew = line.split(',')
    print(" ".join(linenew))
fp.close()