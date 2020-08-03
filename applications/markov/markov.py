import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
l = words.split()
# print(l)
d = {}
f = {}
g = []
x = 0
while x < len(l) - 1:
    # # print(g.append(l[x+1]))
    # word = l[x+1]
    # key = d[l[x]]
    # print(g)
    # if key in d:
    #     key = g.append(word)
    # else: 
    #     key = g
    
    # print(g)

    # d[l[x]] = g.append(word)
    if l[x] in d:
        f[l[x]] += 1
        d[l[x]] += " " + (l[x + 1])
    else:
        f[l[x]] = 1
        d[l[x]] = l[x + 1]
    x += 1 

key = d.keys()
v = d.values()
# v.split()
print(key)

    
# items = list(d.items())
# items.sort()
# print(items)
    # print(x)
    # print(l[x])    
# print(d)
# print(f)
    


# TODO: construct 5 random sentences
# Your code here

