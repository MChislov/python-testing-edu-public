
#Vasya implemented nonoptimal Enum classes.
#Remove duplications in variables declarations using metaclasses.

from enum import Enum

class SimplifiedEnum(type):
    keys_dict_key = '_' + class_name + '__keys'
    keys = attributes[keys_dict_key]
    for key in keys:
        setattr(None, key, key)
    print(keys)

class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"


#Should become:

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
