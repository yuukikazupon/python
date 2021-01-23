dict = {"a": [1, 2], "b": [1, 3], "c": [1, 4]}
a=dict.items()
print(a)
c=[y[0] for y in filter(lambda x: 4 in x[1],a)]
print(c)

b=[["taro"],[]]
print(len(b[1]))
