"""
Create classes to track homeworks.

1. Homework - accepts howework text and deadline (datetime.timedelta)
Homework has a method, that tells if deadline has passed.

2. Student - can solve homework with `do_homework` method.
Raises DeadlineError with "You are late" message if deadline has passed

3. Teacher - can create homework with `create_homework`; check homework with `check_homework`.
Any teacher can create or check any homework (even if it was created by one of colleagues).

Homework are cached in dict-like structure named `homework_done`. Key is homework, values are 
solutions. Each student can only have one homework solution.

Teacher can `reset_results` - with argument it will reset results for specific homework, without - 
it clears the cache.

Homework is solved if solution has more than 5 symbols.

-------------------
Check file with tests to see how all these classes are used. You can create any additional classes 
you want.
"""
import datetime

class DeadlineError(Exception):
    def __init__(self, message='You are late'):
        super(DeadlineError, self).__init__(message)


class Homework():
    def __init__(self, name : str, deadline_delta : int):
        self.name = name
        self.deadline_delta = deadline_delta

    def final_datetime(self):
        return datetime.datetime.now()+datetime.timedelta(minutes=self.deadline_delta)

    def is_deadline_passed(self) -> object:
        if datetime.datetime.now()>self.final_datetime():
            raise DeadlineError("You are late")
        else:
            return "Just in time"

class Student():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def do_homework(self, hw : Homework, solution : str):
        hw.is_deadline_passed()
        return Result(hw, self, solution)

class Result:
    def __init__(self, hw: Homework, author: Student, solution: str):
        self.hw = hw
        self.author = author
        self.solution = solution

class Teacher:
    homework_done = {}

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def create_homework(name: str, deadline_shift: int):
        return Homework(name, deadline_shift)

    def check_homework(self, result: Result):
        if result.hw in Teacher.homework_done.keys():
            if result in Teacher.homework_done[result.hw]:
                return True
        else:
            Teacher.homework_done[result.hw]=[]
        if len(result.solution)>5:
            Teacher.homework_done[result.hw].append(result)
            return True
        else:
            return False

    def reset_results(*args):
        if len(args) == 0:
            Teacher.homework_done={}
        else:
            Teacher.homework_done.remove(args[0])