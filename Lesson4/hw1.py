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
        return Teacher.send_homework_to_teacher(self, hw, solution)

class Result:
    def __init__(self, author: Student, solution: str):
        self.author = author
        self.solution = solution

class Teacher:
    homework_done = {}

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @classmethod
    def send_homework_to_teacher(self, author: Student, hw: Homework, solution: str):
        if hw in Teacher.homework_done.keys():
            Teacher.homework_done[hw].append(Result(author, solution))
        else:
            Teacher.homework_done[hw] = [Result(author, solution)]
        return Teacher.homework_done[hw][-1]

    def create_homework(name: str, deadline_shift: int):
        return Homework(name, deadline_shift)

    def check_homework(self, result: Result):
        if len(result.solution)>5:
            return True
        else:
            return False

    def reset_results(*args):
        if len(args) == 0:
            Teacher.homework_done={}
        else:
            Teacher.homework_done.remove(args[0])

first_teacher = Teacher("Kay", "Alan")
second_teacher = Teacher("Liskov", "Barbara")
first_student = Student("Hopper", "Grace")
second_student = Student("Turing", "Alan")
first_hw = Teacher.create_homework("OOP homework", 1)
second_hw = Teacher.create_homework("Read the documentation", 5)

result_1 = first_student.do_homework(first_hw, "Homework 1 is done")
result_2 = second_student.do_homework(second_hw, "done")

print()
print(type(result_1))