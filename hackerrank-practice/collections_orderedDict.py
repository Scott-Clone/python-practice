from collections import OrderedDict

n = int(input())

od = OrderedDict()
for _ in range(n):
    item, _, price = input().rpartition(' ')
    od[item] = od.get(item, 0) + int(price)
    
for item, price in od.items():
    print(f'{item} {str(price)}')
