import pprint
d = dict()

# histogram()
def histogram(line):
    return line.replace(",","").replace("\r","").replace("\n","").replace("!","").replace("?","").replace(".","").replace("\'","").replace("\"","")

with open("chill.txt", "r") as fp:
  
  line = fp.readline()
  
  for word in histogram(line).split(" "):
    if not word in d:
        d[word] = 0
    d[word] += 1
  print(line)
  while line:
    line = fp.readline()
    
    for word in histogram(line).split(" "):
      if not word in d:
        d[word] = 0
      d[word] += 1

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(d)

# unique_words():
c = 0 
for k, v in d.items():
  c+= 1

print(c) 

def frequency(word, histogram):
    # search keyword histogram
    return histogram[word]
pp.pprint(frequency("with", d))