import re

count = int(input())
myList = []

for _ in range(count):
    myList.append(input())

for item in myList:
    try:
        re.compile(item)
        print(True)
    except re.error:
        print(False)

"""
Task:

You are given a string .
Your task is to find out whether  is a valid regex or not.

Input Format

The first line contains integer , the number of test cases.
The next  lines contains the string .

Constraints


Output Format

Print "True" or "False" for each test case without quotes.

Sample Input

2
.*\+
.*+
Sample Output

True
False
Explanation

.*\+ : Valid regex.
.*+: Has the error multiple repeat. Hence, it is invalid.
"""