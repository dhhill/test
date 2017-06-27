def counter(l):
    i = 0;
    while i < len(l):
        word = l[i]
        number = l.count(word)
        print("word: %r\t %r \n" % (word, number))
        l = remove_value(l,word)
        i += 1

def remove_value(l,value):
    return [val for val in l if val != value]

def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

List = read_words("quotes.list")
counter(List)