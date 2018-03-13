list = []
for i in range(1, 20):
    list.append(i)
    if len(list) > 10:
        list.pop(0)
    else:
        pass
    print list
