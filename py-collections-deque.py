from collections import deque
d = deque()

n = int(input())

for _ in range(n):
    command = input().split()
    operation = command[0]
    args = command[1:]
    getattr(d, operation)(*map(int, args))
    
print(*d)

"""
Task

Perform append, pop, popleft and appendleft methods on an empty deque .

Input Format

The first line contains an integer , the number of operations.
The next  lines contains the space separated names of methods and their values.

Constraints


Output Format

Print the space separated elements of deque .

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft
Sample Output

1 2
"""