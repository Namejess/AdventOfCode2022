import re

if __name__ == '__main__':
    with open('input') as f:
        listInput = f.read().split('\n\n')
        Sum = [sum(map(int, re.findall('\d+', block))) for block in listInput]

p1 = max(Sum)
p2 = sum(sorted(Sum, reverse=True)[:3])
print(p1)
print(p2)

