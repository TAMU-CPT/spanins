from ast import literal_eval as make_tuple

scores = [18, 16, 14, 13, 11, 10, 8, 7, 0]

# embedded_unique
# data = {
    # "(11, 8)":3,
    # "(16, 18)":4,
    # "(13, 0)":1,
    # "(14, 18)":7,
    # "(8, 8)":2,
    # "(0, 11)":1,
    # "(10, 10)":3,
    # "(8, 0)":5,
    # "(11, 11)":4,
    # "(0, 13)":2,
    # "(8, 10)":9,
    # "(7, 8)":1,
    # "(16, 16)":1,
    # "(13, 18)":1,
    # "(13, 16)":1,
    # "(10, 7)":1,
    # "(8, 11)":6,
    # "(13, 8)":4,
    # "(11, 16)":1,
    # "(14, 13)":6,
    # "(11, 0)":1,
    # "(13, 10)":4,
    # "(13, 13)":26,
    # "(8, 13)":9,
    # "(14, 0)":6,
    # "(10, 8)":3,
    # "(0, 10)":1,
    # "(10, 11)":8,
    # "(16, 0)":1,
    # "(11, 10)":1,
    # "(10, 13)":12,
    # "(8, 18)":1,
    # "(14, 10)":4,
    # "(18, 8)":1,
    # "(14, 14)":2,
    # "(13, 11)":5,
    # "(14, 8)":7
# }

# embedded_non_unique
# data = {
    # "(11, 8)":3,
    # "(16, 18)":4,
    # "(13, 0)":1,
    # "(14, 18)":11,
    # "(8, 8)":2,
    # "(0, 11)":1,
    # "(10, 10)":3,
    # "(8, 0)":5,
    # "(11, 11)":4,
    # "(0, 13)":2,
    # "(8, 10)":9,
    # "(7, 8)":1,
    # "(16, 16)":1,
    # "(13, 18)":1,
    # "(13, 16)":1,
    # "(10, 7)":1,
    # "(8, 11)":6,
    # "(13, 8)":4,
    # "(11, 16)":1,
    # "(14, 13)":6,
    # "(11, 0)":1,
    # "(13, 10)":4,
    # "(13, 13)":31,
    # "(8, 13)":13,
    # "(14, 0)":6,
    # "(10, 8)":3,
    # "(0, 10)":1,
    # "(10, 11)":13,
    # "(16, 0)":1,
    # "(11, 10)":1,
    # "(10, 13)":16,
    # "(8, 18)":1,
    # "(14, 10)":4,
    # "(18, 8)":1,
    # "(14, 14)":2,
    # "(16, 8)":1,
    # "(13, 11)":5,
    # "(14, 8)":10
# }

# overlapping_unique
# data = {
    # "(11, 8)":10,
    # "(10, 14)":9,
    # "(11, 18)":8,
    # "(8, 8)":6,
    # "(0, 11)":2,
    # "(10, 10)":3,
    # "(11, 11)":6,
    # "(0, 13)":1,
    # "(8, 10)":3,
    # "(11, 13)":3,
    # "(13, 14)":1,
    # "(13, 18)":2,
    # "(16, 14)":1,
    # "(8, 11)":18,
    # "(13, 8)":6,
    # "(14, 13)":3,
    # "(16, 10)":1,
    # "(18, 11)":1,
    # "(13, 10)":3,
    # "(16, 8)":1,
    # "(8, 13)":6,
    # "(7, 11)":2,
    # "(16, 16)":1,
    # "(10, 8)":14,
    # "(0, 8)":1,
    # "(8, 16)":1,
    # "(0, 10)":2,
    # "(10, 11)":7,
    # "(11, 10)":5,
    # "(10, 13)":19,
    # "(7, 13)":1,
    # "(10, 0)":3,
    # "(13, 11)":10,
    # "(16, 13)":1,
    # "(16, 11)":3,
    # "(13, 13)":20,
    # "(8, 0)":4,
    # "(13, 16)":2
# }

# overlapping_non_unique
# data = {
    # "(11, 8)":11,
    # "(10, 14)":12,
    # "(11, 18)":10,
    # "(8, 8)":7,
    # "(0, 11)":3,
    # "(10, 10)":5,
    # "(11, 11)":7,
    # "(0, 13)":1,
    # "(8, 10)":3,
    # "(11, 13)":3,
    # "(13, 14)":1,
    # "(13, 18)":2,
    # "(16, 14)":1,
    # "(8, 11)":26,
    # "(13, 8)":6,
    # "(14, 13)":3,
    # "(16, 10)":2,
    # "(18, 11)":2,
    # "(13, 10)":3,
    # "(16, 8)":1,
    # "(8, 13)":6,
    # "(7, 11)":2,
    # "(16, 16)":1,
    # "(10, 8)":15,
    # "(0, 8)":1,
    # "(8, 16)":1,
    # "(0, 10)":2,
    # "(10, 11)":7,
    # "(11, 10)":5,
    # "(10, 13)":20,
    # "(7, 13)":1,
    # "(10, 0)":3,
    # "(13, 11)":13,
    # "(16, 13)":1,
    # "(16, 11)":3,
    # "(13, 13)":31,
    # "(8, 0)":4,
    # "(13, 16)":2
# }

# separate_unique
# data = {
    # "(11, 8)":2,
    # "(8, 14)":2,
    # "(13, 0)":1,
    # "(8, 8)":2,
    # "(16, 13)":1,
    # "(11, 11)":3,
    # "(8, 10)":8,
    # "(11, 13)":6,
    # "(16, 16)":1,
    # "(10, 13)":9,
    # "(13, 16)":4,
    # "(11, 16)":5,
    # "(13, 14)":1,
    # "(16, 11)":2,
    # "(13, 10)":13,
    # "(16, 8)":1,
    # "(8, 13)":8,
    # "(10, 8)":2,
    # "(8, 16)":1,
    # "(0, 10)":3,
    # "(10, 11)":2,
    # "(11, 10)":3,
    # "(8, 11)":4,
    # "(0, 0)":1,
    # "(18, 11)":1,
    # "(18, 13)":1,
    # "(13, 13)":7,
    # "(13, 11)":1,
    # "(14, 8)":1,
    # "(10, 10)":3
# }

# separate_non_unique
data = {
    "(11, 8)":4,
    "(8, 14)":3,
    "(13, 0)":1,
    "(8, 8)":2,
    "(16, 13)":1,
    "(11, 11)":3,
    "(8, 10)":8,
    "(11, 13)":6,
    "(16, 16)":1,
    "(10, 13)":11,
    "(13, 16)":4,
    "(11, 16)":5,
    "(13, 14)":1,
    "(16, 11)":3,
    "(13, 10)":18,
    "(16, 8)":1,
    "(8, 13)":8,
    "(10, 8)":2,
    "(8, 16)":1,
    "(0, 10)":3,
    "(10, 11)":2,
    "(11, 10)":4,
    "(8, 11)":4,
    "(0, 0)":1,
    "(18, 11)":5,
    "(18, 13)":1,
    "(13, 13)":7,
    "(13, 11)":2,
    "(14, 8)":1,
    "(10, 10)":3
}

ls = []
for s in range(0,19):
    ls.append([0 for s in range(0,19)])

for d in data:
    tup = make_tuple(d)
    if tup[0] == None or tup[1] == None:
        continue
    ls[tup[1]][tup[0]] = data[d]

# import pprint; pprint.pprint(ls)

print "labels", '\t',
for s in scores:
    print str(s) + 'o', '\t',
print '\n'

for s in scores[::-1]:
    print str(s) + 'i', '\t',
    for t in scores:
        print ls[t][s], '\t',
    print '\n'
