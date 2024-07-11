arr = [33, 456, "sadkljdslk", "djks", [3, 4, 53, 3, 2], (3, 5, 234, 4)]

a = {}

for i in arr:
    type_name = type(i).__name__
    if type(i) in a:
        a[type_name].append(i)
    else:
        a[type_name] = [i]

print(a)
