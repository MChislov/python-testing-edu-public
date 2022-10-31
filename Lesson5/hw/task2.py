import sqlite3
conn = sqlite3.connect('example.sqlite')
cursor = conn.cursor()
data = cursor.execute('SELECT name FROM sqlite_master')
data = cursor.fetchall()
print(data)# will be a list with data.
length = cursor.execute('SELECT count(*) FROM presidents')
print(length.fetchone()[0])


class RequestTableData():
    def __init__(self, database_path: str, table_name=None, data_filter=None):
        self.database_path = database_path
        self.table_name = table_name
        self.data_filter = data_filter
        self.cursor = self.connect_to_database(database_path)

    def connect_to_database(self, database_path):
        conn = sqlite3.connect(database_path)
        return conn.cursor()

    def request_table_data(self, database_path, table_name, data_filter):
        db_cursor = self.connect_to_database(self, database_path)
        if data_filter!=None:
            data = db_cursor.execute('SELECT name FROM ' + table_name + ' where name LIKE \'%' + data_filter + '%\'')
        else:
            data = db_cursor.execute('SELECT name FROM ' + table_name)

        return data


class TableData():
    def __init__(self, database_name: str, table_name: str, data_filter=None):
        self.database_name = database_name
        self.table_name = table_name
        self.data_filter = data_filter
        self.db_cursor = RequestTableData(database_name).cursor
        #self.__dict__ = self.get_dict_data(self.path)

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        print('key=' + str(key))
        if key != 0:
            result = self.db_cursor.execute('SELECT * FROM ' + self.table_name + ' where name LIKE \'%' + key + '%\'')
            return result.fetchone()
        else:
            result = self.db_cursor.execute('SELECT * FROM ' + self.table_name)
            return result.fetchall()

    def __len__(self):
        length = self.db_cursor.execute('SELECT count(*) FROM ' + self.table_name)
        return (length.fetchone()[0])

tableDataItem = TableData('example.sqlite', 'presidents')
print(len(tableDataItem))
print(tableDataItem['Yeltsin'])

presidents = TableData(database_name='example.sqlite', table_name='presidents')
boolean = ('Yeltsin' in presidents)
