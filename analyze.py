import random as rand

letters = ['(', ')']

for name in open('names.txt', 'r'):
    for c in name.strip('\n'):
        if c not in letters:
            letters.append(c)

print('Letters:')
print(letters)

prob_matrix = [[0 for j in range(len(letters))] for k in range(len(letters))] #init n*n matrix

for name in open('names.txt', 'r'):
    name = '(' + name.strip() + ')'
    for i in range(1, len(name)):
        prob_matrix[letters.index(name[i-1])][letters.index(name[i])] += 1


#print('Matrix:')
#print(prob_matrix)

#GENERATE STRING#
def get_name():
    name = "("

    while name[-1] != ')':
        line = prob_matrix[letters.index(name[-1])]
        total = sum(line)
        n = rand.randint(0, total-1)
        for i in range(0, len(line)):
            n -= line[i]
            if n < 0:
                name += letters[i]
                break
    return name.strip("()")



for i in range(100):#while input() != 'q':
    print(get_name())
