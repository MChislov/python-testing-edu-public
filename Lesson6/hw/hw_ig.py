# 1. Implement a function that flatten incoming data:
# non-iterables and elements from iterables (any nesting depth should be supported)
# function should return an iterator (generator function)
# don't use third-party libraries

def merge_elems(*elems):

    def check_all_elements_are_flat(input_item):
        isiterable = hasattr(input_item, '__iter__')
        if isiterable:
            for item in input_item:
                if hasattr(item, '__iter__') and (len(item)) > 1:
                    return False
        return True

    def flatten_element(input_item):
        for element_flatten in input_item:
            if hasattr(element_flatten, '__iter__') and (len(element_flatten)) > 1:
                element_index = input_item.index(element_flatten)
                input_item.pop(element_index)
                for item_index in range(len(element_flatten)):
                    input_item.insert(item_index + element_index, element_flatten[item_index])
        return input_item

    for item in elems:
        if hasattr(item, '__iter__'):
            while not check_all_elements_are_flat(item):
                item = flatten_element(item)
            for element in item:
                yield element
        else:
            yield item


# example input
a = [1, 2, 3]
b = 6
c = 'zhaba'
d = [[1, 2], [3, 4]]

for _ in merge_elems(a, b, c, d):
    print(_, end=' ')

# output: 1 2 3 6 z h a b a 1 2 3 4

print('\nNext task:')


# 2. Implement a map-like function that returns an iterator (generator function)
# extra functionality: if arg function can't be applied, return element as is + text exception

def map_like(fun, *elems):
    for item in elems:
        try:
            yield fun(item)
        except TypeError as e:
            yield str(item) + ' ' + str(e)


# example input
a = [1, 2, 3]
b = 6
c = 'zhaba'
d = True
fun = lambda x: x[0]

for _ in map_like(fun, a, b, c, d):
   print(_)

# output:
# 1
# 6: 'int' object is not subscriptable
# z
# True: 'bool' object is not subscriptable
