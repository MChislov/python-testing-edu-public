# https://www.python.org/dev/peps/pep-0570/#logical-ordering
# Positional-only parameters also have the (minor) benefit of enforcing some logical order when
# calling interfaces that make use of them. For example, the range function takes all its
# parameters positionally and disallows forms like:

# range(stop=5, start=0, step=2)
# range(stop=5, step=2, start=0)
# range(step=2, start=0, stop=5)
# range(step=2, stop=5, start=0)

# at the price of disallowing the use of keyword arguments for the (unique) intended order:

# range(start=0, stop=5, step=2)
"""
Write a function that accept any sequence (list, string, tuple) of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
import string

"""class custom_range:
    def __init__(self, initial_collection, last_element):
        self.initial_collection = initial_collection
        self.last_element = last_element
        self.first_element = None
        self.step = 1

    def __init__(self, initial_collection, first_element,  last_element):
        self.initial_collection = initial_collection
        self.last_element = last_element
        self.first_element = first_element
        self.step = 1

    def __init__(self, initial_collection, first_element,  last_element, step):
        self.initial_collection = initial_collection
        self.last_element = last_element
        self.first_element = first_element
        self.step = step

    def get_slice_config(self):
        last_index = self.initial_collection.index(self.last_element)
        if self.first_element!=None:
            first_index = self.initial_collection.index(self.first_element)
        else:
            first_index=0
        return first_index+"\:"+last_index+"\:"+self.step

    def return_substring(self):
        return self.initial_collection.slice(self.get_slice_config())"""

def custom_range(*args):
    if len(args) == 2: slice_exp = slice(list(args[0]).index(args[1]))
    if len(args) == 3: slice_exp = slice(list(args[0]).index(args[1]), list(args[0]).index(args[2]))
    if len(args) == 4: slice_exp = slice(list(args[0]).index(args[1]), list(args[0]).index(args[2]), args[3])
    return list(args[0])[slice_exp]