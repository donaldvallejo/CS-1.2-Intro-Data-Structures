import random

f = open("shortlist.txt", "r")
shortlist = f.readlines() 
d = {}

for line in shortlist:
    word_list = line.lower().replace("\n","").split(" ")
    for word in word_list: 
        d[word] = d.get(word, 0) + 1

word_freq = []

count_freq = {}
total_count = 0
for key, value in d.items():
    total_count += value
    count_freq[key] = 0
    word_freq.append([value, key])

#print(word_freq)
num = 10000
for i in range(num):
    # try to pick a word randomly
    print("Random choice")
    # print(random.choice(word_freq))
    index = random.randint(0,len(word_freq)-1)
    print(index)
    #print(word_freq[index])
    count_freq[word_freq[index][1]] += 1

print(count_freq)

# divide total by two 

## for each word in word_freq, do divide that freq/total_count
# for word in word_freq:
#    probability = word[0] / total_count
#    print(word[1], probability)