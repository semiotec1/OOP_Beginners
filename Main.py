def hello():
    print("Hello")
x = 1
y = "Hello"
print(y.upper())

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("bark")
    def add_one(self, x):
        return x + 1
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age

print("test")

d = Dog("Tim", 5)
d.set_age(12)
print(d.get_age())

#Example 2 OOP

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade #0 - 100
    def get_grade(self):
        return self.grade
class Course:
    def __init__(self, name , max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value /len(self.students)


#Our three students we created with name, age and grade
s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill",19,65)
#Our course with name and max students
course = Course("Science",2)
#Add students to course
course.add_student(s1)
course.add_student(s2)
#See first student in course
print(course.students[0].name)
#average grade of all the students
print(course.get_average_grade())