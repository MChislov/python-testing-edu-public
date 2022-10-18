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


def check_five_entries_in_line(line: str) -> bool:
    pattern_five_entries = "([\S]*)\ ([\S]*)\ ([\S]*)\ ([\S]*)\ ([\S]*)"
    x = re.search(pattern_five_entries, line)
    if x==None:
        return "Line does not contain 5 groups"
    else:
        return None

def validate_date(date: str) -> bool:
    pattern_date = "([\S]*)$"
    date_block = re.search(pattern_date, date)
    if date_block==None:
        return "There is no valid date block for analysis in the expected position"
    pattern_year_month_day = "(\d{4})\-(\d{2})\-(\d{2})"
    split_date = re.search(pattern_year_month_day, date_block.group(1))
    if split_date==None:
        return "There is invalid date format"
    try:
        datetime.strptime(split_date.string, '%Y-%m-%d').date()
    except:
        return "There is no valid date in the account information"
    finally: return None


def validate_line(line: str) -> bool:
    return True





def check_data(filepath: str, validators: Iterable[Callable]) -> str:
    result_file_path = "./result_file.txt"
    result_file = open(result_file_path, "w+")
    with open("./data.txt") as ifile:
        index = 0
        for line in ifile:
            result_file.write(line.strip() + "\n")
            result_file.write("line with index: " + index.__str__() + " validation failures:")
            for validator in validators:
                validation_result = validator(line.strip())
                if validation_result != None: result_file.write(validation_result)
            result_file.write("\n")
            index+=1
    result_file.flush()
    result_file.close()
    return result_file_path

check_data("./data.txt", [validate_date])


