count = 0
name = input("Enter file:")
handle = open(name)
di = dict()
lin = list()
for line in handle :
    if line.startswith('From'):
        if line.startswith('From: '):
            continue
        else :
            count = count+1
            words = line.split()
            str1 = ''.join(words[5])
            lin.append(str1[0:2])
for word in lin:
    di[word] = di.get(word,0)+1
for i,y in sorted(di.items()):
    print(i,y)
