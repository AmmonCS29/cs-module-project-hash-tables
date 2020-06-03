# Lookup Table

For expensive operations, caching the results in a lookup table speeds
future queries.

The lookup table can be built in advance by iterating over all values in
the _domain_ of the function and recording the results.

Or, more lazily, can be build as the individual values are passed in.

Modify the code in this directory to build a lookup table so that it can
finish running in under a minute.

There's no test file for this. It's counting to 50,000, so if it
finishes before you give up, then you're golden.


## Understanding

Caching expensive operations in a look up table speeds up future queries. 

Build a table in advance by iterating over all the values in the domain of the function and record he results. Or do it as you go while looking up the values. 

## Planning
import math

Create a look_up_table dictionary. 

create a function called slowfun
    iterate over a table of a range of 1000
    find the index in the table and assign it the factorial of the number. 

