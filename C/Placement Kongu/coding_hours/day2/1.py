import re
r = re.compile('^[^0-9]\w{4,}')
x = r.findall(input())
print(1 if x else 0)
