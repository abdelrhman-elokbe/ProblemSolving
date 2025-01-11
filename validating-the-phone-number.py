import re

expression = r'^[789]\d{9}$'
n = int(input())

for _ in range(n):
    if re.match(expression, input()):
        print("Yes")
    else:
        print("NO")