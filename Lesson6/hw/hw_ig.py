# 1. Implement a function that flatten incoming data:
# non-iterables and elements from iterables (any nesting depth should be supported)
# function should return an iterator (generator function)
# don't use third-party libraries

def merge_elems(*elems):
    output = list(elems)
    def check_all_elements_are_flat(current_list: list):
        for item in current_list:
            isiterable = hasattr(item, '__iter__')
            if isiterable:
                if len(item) > 1:
                    return False
        return True

    def get_index_of_iterable(current_list: list):
        for item in current_list:
            isiterable = hasattr(item, '__iter__')
            if isiterable:
                if  len(item)>1:
                    return current_list.index(item)

    def flatten_element(current_list: list, index: int):
        iterable = current_list.pop(index)
        for item_index in range(len(iterable)):
            current_list.insert(index+item_index, iterable[item_index])
        return current_list

    while not check_all_elements_are_flat(output):
        output = flatten_element(output, get_index_of_iterable(output))

    return output

# example input
a = [1, 2, 3]
b = 6
c = 'zhaba'
d = [[1, 2], [3, 4]]

for _ in merge_elems(a, b, c, d):
    print(_, end=' ')

# output: 1 2 3 6 z h a b a 1 2 3 4

# 2. Implement a map-like function that returns an iterator (generator function)
# extra functionality: if arg function can't be applied, return element as is + text exception

def map_like(fun, *elems):
    pass

# example input
a = [1, 2, 3]
b = 6
c = 'zhaba'
d = True
fun = lambda x: x[0]

#for _ in map_like(fun, a, b, c, d):
#    print(_)

# output:
# 1
# 6: 'int' object is not subscriptable
# z
# True: 'bool' object is not subscriptable