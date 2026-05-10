import random
from school import School
class Person:
    def __init__(self,name):
        self.name = name


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name) 

    def evaluate_exam(self):
        return random.randint(1,100)


class Student(Person):
    def __init__(self, name,classroom):
        super().__init__(name)
        self.classroom = classroom
        self__id = None
        self.marks = {} # {english:78,"bangla":90}
        self.subject_grade = {} # {english:"A"}
        self.grade = None # final grade

    
    def final_grade(self):
        sum = 0
        for grade in self.subject_grade.values():
            point = School.grade_to_value(grade) # 5.00
            sum += point
        gpa = sum / len(self.subject_grade) # 7/2 = 3.50
        self.grade = School.value_to_grade(gpa)
        
    @property
    def id(self):
        return self.__id 
        
    @id.setter
    def id(self,value):
        self.__id = value