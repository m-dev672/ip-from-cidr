import random

cidr = '10.109.101.0/24'

networkip = sum([int(e) << i for i, e in zip([24, 16, 8, 0], cidr.split('/')[0].split('.'))])
mask = 2 ** int(cidr.split('/')[1]) - 1 << 32 - int(cidr.split('/')[1])

iprange = range((networkip & mask), networkip | (~mask & 4294967295))

reservedip = [
    iprange[0],
    iprange[-1]
]

address = random.choice(list(set(iprange) - set(reservedip)))

print('.'.join([str((address << i & 4294967295) >> 24) for i in [0, 8, 16, 24]]))