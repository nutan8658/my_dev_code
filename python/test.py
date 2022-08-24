string_name = "aaabbcdccffe"
l1 = list()
  
# Iterate over the string
for element in string_name:
    if len(l1) == 0:
        l1.append(element)
    elif element == l1[-1]:
        del l1[-1]
    else:
        l1.append(element)


print('hello, test for git')
print('hello, test for git XXXXXX')

print(''.join(l1))
    