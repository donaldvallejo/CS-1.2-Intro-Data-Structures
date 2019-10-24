import random
import sys

num_of_words = int(sys.argv[1])
print(num_of_words)

fp = open('words', 'r')
line = fp.readline()
lines = []
cnt = 1
while line:
    line = fp.readline()
    print(line)
    lines.append(line.strip()) 
    cnt += 1
lines = lines[:-1]

def random_python_quote():
    for line in lines:
        rand_index = random.randint(0, len(lines) - 1)
    return lines[rand_index]

if __name__ == '__main__':
    print(lines)
    random.shuffle(lines)
    a = ' '.join(lines[0:num_of_words])
    print(a)