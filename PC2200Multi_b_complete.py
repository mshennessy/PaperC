# PC2200 Multi (b)
# Name and School: 

fp=open("PC2200Multi_b.csv",'r')

fullFile = fp.readlines()
print("Subject\t\tMarks")
for line in fullFile:
    newLine=line.strip('\n')
    finalLine=newLine.split(',')
    print(finalLine[0],'\t\t',finalLine[1])

fp.close()