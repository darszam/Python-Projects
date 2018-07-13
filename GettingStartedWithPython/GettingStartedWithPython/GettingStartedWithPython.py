# Lists test
tst_list = ['test1', 'test2', 3]
for element in tst_list:
    print(element)
del tst_list[1]
for element in tst_list:
    print(element)

# Tuples
tst_tuple = 'element1', 'element2', 'element3'
for element in tst_tuple:
    print(element)

# Dictionary
dictionary = {'key1':'value1','key2':'value2'}
print(dictionary['key1'])
del dictionary['key1']
print (dictionary)

# Set
tst_set = set(['Jane','Mark','Stephen'])
print(tst_set)