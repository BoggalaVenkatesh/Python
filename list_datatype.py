#list

# it is a collection values

# l = [1, 2, 3, "abc", True, [10, 20, 30, "abc", False]]  #nested list
# print(l, type(l))

# l1 = l[3]
# print(l1)

# l2 = l[5]
# print(l2)

# l3 = l[-1][0]
# print(l3)

# print(l[len(l) - 1][0])

# print(dir(l))

'''
 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
 
 '''
l = [10, 20, 30, "abc", False]

# append an element to the end of the list

l.append(True)
print(l)

l.append([10, 20, 30, "abc", False])
print(l)
