from operator import itemgetter, attrgetter

with open("robin.txt") as f:
    words = f.read()

# print(words)

def word_count(s):
    # Your code here
    counts = {}
    punctuations =  ' : ; , . - + = / \ | [ ] { } ( ) * ^ & " '
    
    
    for x in s: 
        if x in punctuations:
            s = s.replace(x, " ")

    s = " ".join(s.split())
    
    new_s = s.split()    

    for c in new_s:
        c = c.lower()  # case insensitive
        if c in counts:
            counts[c] += '#'
        else:
            counts[c] = '#'

    items = list(counts.items())
    # items.sort(key=lambda e: e[1], reverse= True)
    # items.sort()
    items = sorted(items, key=itemgetter(1), reverse=True)
    # new_items.sort()
    # items.sorted(key= itemgetter(1, -2), reverse=True)
    return items

print(word_count(words))