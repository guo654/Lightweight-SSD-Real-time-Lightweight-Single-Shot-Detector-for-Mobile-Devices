s =[]
f = open('/home/jari/guoshi/workspace/mobilenetssd/models-master/research/object_detection/dataset_tools/a.txt','r')
for lines in f:
    ls = lines.replace('[','').replace('b','').replace('\'','').replace('\'','').replace(']','').strip('\n')
    if len(ls) < 12:
        ls = ls.zfill(12)
    s.append(ls)
f.close()
print(s)


f1 = open('/home/jari/guoshi/workspace/mobilenetssd/models-master/research/object_detection/dataset_tools/b.txt','w')
for j in s:
    #f1.write(j+'.jpg'+' '+'\\'+'\n')
    f1.write(j+'.jpg'+'\n')
f1.close()
