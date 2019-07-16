'''Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you.
So, for example, if we define end to be 6, your code should print out the result: 21, which is 1 + 2 + 3 + 4 + 5 + 6.

For problems such as these, do not include input statements or define variables we will provide for you. 
Our automating testing will provide values so write your code in the following box assuming these variables are already defined.
'''

i = 0
result = 0
while i < end:
    i = i+1
    result = result + i
print(result)