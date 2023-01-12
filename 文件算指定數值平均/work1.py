fname = input("Enter file name: ")
fh = open(fname,'r')
import statistics
rey = []
counts = 0
vv = 0
for line in fh:
  line = line.rstrip()
  if line.startswith("X-DSPAM-Confidence: ") :
     y = line.replace('X-DSPAM-Confidence: ','')
     y = float(y)
     rey.append(y)
     counts = counts+y
     vv = vv+1
     zz = (counts/vv)
print ('Average spam confidence: ', zz)
#mbox-short.txt
