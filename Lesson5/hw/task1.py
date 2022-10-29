import re

class storage:
    def __init__(self, path: str):
        self.file_path = path
        self.data = {}

    def KeyValueStorage(path):
        pattern = "([a-zA-Z0-9_]*)\=([a-zA-Z0-9]*)"
        data = {}
        with open(path, 'r') as ifile:
            for line in ifile:
                pair = re.search(pattern, line)
                if re.match('^\d*$', pair.group(2)):
                    value = int(pair.group(2))
                else:
                    value = pair.group(2)
                data.update({pair.group(1):value})
        return data


