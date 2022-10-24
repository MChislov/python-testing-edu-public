"""
check_data function takes two parameters - path to a file and a list of functions (validators).
You should:
- read data from file data.txt
- validate each line according to rules. Each rule is a function, that performs some specific check
- write a report to txt file and return absolute path to that file. For each line you should report 
it if it doesn't conform with at least one rule, plus add a reason - the name of a validator that
doesn't pass (if there are more than one failed rules, get the name of the first one that fails)

Valid line should have 5 elements in this order:
email, amount, currency, account, date

You should also implement at least two rules:
- validate_line should check if a line has 5 elements
- validate_date should check if a date is valid. In our case valid date will be anything that follows
the pattern DDDD-DD-DD (four digits - two digits - two digits). Date always exists in a line, even 
if this line is corrupted in some other way.
Feel free to add more rules!

For example, input lines:
foo@example.com 729.83 EUR accountName 2021-01:0
bar@example.com 729.83 accountName 2021-01-02
baz@example.com 729.83 USD accountName 2021-01-02

check_data(filepath, [validate_date, validate_line])

output lines:
foo@example.com 729.83 EUR accountName 2021-01:0 validate_date
bar@example.com 729.83 accountName 2021-01-02 validate_line
"""
from typing import Callable, Iterable
import re
from datetime import date, datetime
import os
from tempfile import NamedTemporaryFile


def check_five_entries_in_line(line: str) -> str:
    pattern_five_entries = "([\S]*)\ ([\S]*)\ ([\S]*)\ ([\S]*)\ ([\S]*)"
    x = re.search(pattern_five_entries, line)
    if x==None:
        return "Line does not contain 5 groups"
    else:
        return None

def check_date_block(date: str) -> str:
    pattern_date = "([\S]*)$"
    date_block = re.search(pattern_date, date)
    if date_block==None:
        return "There is no valid date block for analysis in the expected position"
    pattern_year_month_day = "(\d{4})\-(\d{2})\-(\d{2})"
    split_date = re.search(pattern_year_month_day, date_block.group(1))
    if split_date==None:
        return "There is invalid date format"
    else:
        return None


def validate_line(line: str) -> bool:
    def __name__():
        return "line validation"

    if check_five_entries_in_line(line)==None:
        return True
    else:
        return False

def validate_date(line:str) -> bool:
    def __name__():
        return "date validation"

    if check_date_block(line)==None:
        return True
    else:
        return False



def check_data(filepath: str, validators: Iterable[Callable]) -> str:
    result_file_path = "./result.txt"
    with open(filepath, 'r') as ifile, open(result_file_path, 'w+') as wfile:
        index = 0
        for line in ifile:
            for validator in validators:
                validation_result = validator(line.strip())
                if validation_result != True: wfile.write("line with index: " + index.__str__()+ " validation failed in method '" + validator.__name__ +"'\n")
                if validation_result != True: break
            index+=1

    return os.path.abspath(result_file_path)

check_data("./data.txt", [validate_date, validate_line])


