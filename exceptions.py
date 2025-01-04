count = int(input())
myList = []

for _ in range(count):
    a, b = input().split()
    myList.append((a, b)) 

for item in myList:
    try: 
        print(int(item[0]) // int(item[1]))
    except ZeroDivisionError as e:
        print(f"Error Code: {e}")
    except ValueError as e:
        print(f"Error Code: {e}")
    
"""Task

You are given two values  and .
Perform integer division and print .

Input Format

The first line contains , the number of test cases.
The next  lines each contain the space separated values of  and .

Constraints

Output Format

Print the value of .
In the case of ZeroDivisionError or ValueError, print the error code.

Sample Input

3
1 0
2 $
3 1
Sample Output

Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3

"""
