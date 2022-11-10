import re


class KeyValueStorage(dict):
    def __init__(self, path: str):
        self.path = path
        self.__dict__ = self.get_dict_data(self.path)

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def get_dict_data(self, path):
        pattern = "([a-zA-Z0-9_]*)\=([a-zA-Z0-9]*)"
        data = {}
        with open(path, 'r') as ifile:
            for line in ifile:
                pair = re.search(pattern, line)
                if re.match('^\d*$', pair.group(1)):
                    raise ValueError('Integer provided as a key')
                if re.match('^\d*$', pair.group(2)):
                    value = int(pair.group(2))
                else:
                    value = pair.group(2)
                data.update({pair.group(1): value})
        for key, value in data.items():
            setattr(KeyValueStorage, key, value)
        return data


storage = KeyValueStorage('./task1.txt')


print(storage['name'])
print(storage.song_name)
print(storage.power)
