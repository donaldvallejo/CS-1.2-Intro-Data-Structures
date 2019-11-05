from random import randint
# declares values
f = open("shortlist.txt", "r")
shortlist = f.readlines() 
word_list = []
count = []

# appends all index numbers to the count variable
for i in range(len(shortlist)):
    count.append(0)

# replaces \n and appends strings to the word_list variable
for word in shortlist:
    word = word.replace("\n","")
    word_list.append(word)
    word_list

# takes the lenth of list minus 1 and adds a count of each instance in the count variable
for i in range(10000):
    random_index = randint(0, len(word) - 1)
    count[random_index] += 1

# print for the range of he list, print both index of word_list and count 
for i in range(len(word_list)):
    print(count[i], word_list[i])