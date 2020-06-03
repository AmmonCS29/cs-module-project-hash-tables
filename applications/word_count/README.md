# Count the words in an input string

## Input

This function takes a single string as an argument.

```
Hello, my cat. And my cat doesn't say "hello" back.
```

## Output

It returns a dictionary of words and their counts:

```
{'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}
```

Case should be ignored. Output keys must be lowercase.

Key order in the dictionary doesn't matter.

Split the strings into words on any whitespace.

Ignore each of the following characters:

```
" : ; , . - + = / \ | [ ] { } ( ) * ^ &
```

If the input contains no ignored characters, return an empty dictionary.


## Understanding

Takes in a string of words. 

ouputs a dictionary of words as the key and the count as the value. 

case should be ignored and outputs are lowercase. 

## Planning

create empty dictionary called count
remove the punctation from the string and create a new string 
Then split the new string into another string. 
Then input the keys into a dictionary and the values as the count. 
iterate over the string 