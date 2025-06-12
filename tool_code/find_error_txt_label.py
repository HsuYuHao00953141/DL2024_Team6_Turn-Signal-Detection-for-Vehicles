import os
import re
# 路径
path = "D:\\datasets\\sea_urchin_datasets\\sea_urchin\\Tripneustes_gratilla\\original_labeled\\"
wordname = '4'
sum = 0
# 文件列表
files = []
for file in os.listdir(path):
    if file.endswith(".txt"):
        files.append(path+file)


for file in files:
    file = open(file,'r')
    for line in file:
        data = line.split()
#print(data)
    if wordname in data:
    #print(data.count(wordname))
        sum += 1

print(sum)

file.close()




        

