#Imports
#import matplotlib.pyplot as plt

#Data functions
def frequency(l):
    freq = []
    for i in range(0,len(l)-1):
        j = 0
        while j < len(freq)-1 and freq[j][0] != l[i]:
            j += 1
        if j != 0 and freq[j][0] == l[i]:
            freq[j][1] += 1
        else:
            freq.append([l[i],1])
    return sort_by_second_value(freq)

def consecutive_freq(word,l):
    consecutive = []
    for i in range(0,len(l)-1):
        if l[i] == word:
            j = 0
            while j < len(consecutive)-1 and consecutive[j][0] != l[i+1]:
                j += 1
            if j != 0 and consecutive[j][0] == l[i+1]:
                consecutive[j][1] += 1
            else:
                consecutive.append([l[i+1],1])
    return sort_by_second_value(consecutive)

def phrase_finder2(l):
    phrase = []
    for i in range(0,len(l)-2):
        book_phrase = l[i] + ' ' + l[i+1]
        j = 0
        while j < len(phrase)-1 and phrase[j][0] != book_phrase:
            j += 1
        print(i)
        if j != 0 and phrase[j][0] == book_phrase:
            phrase[j][1] += 1
        else:
            phrase.append([book_phrase,1])
    return sort_by_second_value(phrase)

def make_sentance(start,d):
    print(start)
    used = [start]
    while d[start][0][1] > 1:
        i = 0
        while d[start][i][0] in used:
            i += 1
        print(d[start][i][0])
        used.append(d[start][i][0])
        start = d[start][i][0]

#Helper
def grapher(l):
    plt.plot([row[0] for row in l])
    plt.show()

def make_dict(freq,l):
    d = {}
    for elem in freq:
        d[elem[0]] = consecutive_freq(elem[0],l)
    return d


def sort_by_second_value(l):
    for i in range(1,len(l)):    
        j = i
        while j != 0 and l[i][1] > l[j-1][1] :
            j -= 1
        temp = l[i]
        l.remove(l[i])
        l.insert(j,temp)
    return l

def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

def list_printer(l):
    for elem in l:
        if elem[1] > 2:
            print(elem)

sequence = dict
List = read_words("text")
print(len(List))
#frequent = frequency(List)
#list_printer(frequent)
phrases = phrase_finder2(List)
list_printer(phrases)
#sequence = make_dict(frequent,List)
#make_sentance('I',sequence)