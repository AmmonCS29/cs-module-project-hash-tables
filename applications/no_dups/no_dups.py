def no_dups(s):
    # Your code here
    d ={}
    l = s.split()
    new_l= []
    new_str=" "
    for x in l:
        d[x] = x
    new_l = [k for k in d]
    new_str = " ".join(new_l)

    return new_str

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))