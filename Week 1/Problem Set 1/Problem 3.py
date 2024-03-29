'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart. 
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. 
If you have time, come back to this problem after you've had a break and cleared your head.
'''

string = ""
count = 0
maxcount = 0
maxstring = ""

for i in range(len(s)):
    if i == 0:
        string += s[i]
        count += 1
    elif s[i] >= s[i - 1]:
        string += s[i]
        count += 1
    elif s[i] < s[i - 1]:
        if count > maxcount:
            maxcount = count
            maxstring = string
        count = 0
        count = 1
        string = ""
        string += s[i]
    if i == len(s) - 1:
        if count > 1:
            if count > maxcount:
                maxcount = count
                maxstring = string
                
print("Longest substring in alphabetical order is: " + maxstring)