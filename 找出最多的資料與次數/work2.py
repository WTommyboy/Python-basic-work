name = input("Enter file:")
handle = open(name)
counts = dict()
list1 = list()
for line in handle:
    if line.startswith('From'):
       if line.startswith('From:'):
           continue
       else:
           word = line.split()
           list1.append(word[1])
for word in list1:
    counts[word] = counts.get(word,0)+1

aa = None
bb = None
for word,count in counts.items():
    if aa is None or count > aa:
        bb = word
        aa = count

print(b,a)
