import random
import pprint
pp = pprint.PrettyPrinter(indent=4)

def sampling():
    for line in shortlist:
        word_list = line.lower().replace("\n","").split(" ")
        for word in word_list: 
            d[word] = d.get(word, 0) + 1


    total_count = 0
    count_freq = {}
    
    for key, value in d.items():
        total_count += value
        count_freq[key] = 0
        word_freq.append([value, key])


    num = 10000
    for i in range(num):
        # try to pick a word randomly
        index = random.randint(0,len(word_freq)-1)
        count_freq[word_freq[index][1]] += 1

    # print("count_freq",count_freq)   
    # print("total count",total_count)
    return [count_freq, total_count]


#for weighted numbers to check randomness
def weight(total_count):
    weight_list = []
    #pass
    #print(word_freq)    
    for word_arr in word_freq: 
        # finding probability distribution
        weight_list.append(word_arr[0]/total_count[1])
        print("total_count", weight_list)
    return weight_list


# random generator for the size of the sentence
# make an empty string called sentence
# loop throught the length of the string
# inside that loop pick another random number that is in th size of the histogram
# word_freq[X]
# sentence = sentence + " " + word_freq[x]
# outside of loop add sentence += "."
def select_words(count_freq, total_count):
    sentence = ""
    i = 20
    while i > 0:
        dart = random.random()
        dart_placement = 0
        # print("dart, dart, dart, dart, dart, dart",dart)
        for k , v in count_freq.items():
            prob = v / 1896
            if dart_placement >= dart:
                sentence += " " + k
                break
            dart_placement += prob
        i -= 1
    print(sentence.strip('.@,\"'))
    return sentence
    
if __name__ == "__main__":    
    f = open("chill.txt", "r")
    shortlist = f.readlines()
    d = {}
    word_freq = []
    sample = sampling()
    weight(sample)
    select_words(sample[0], sample[1])
