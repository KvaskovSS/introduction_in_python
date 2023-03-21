import random

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = []

    def __str__(self):
        return f"{self.name} {self.surname}, возраст {self.age}"

    def greet(self):
        print(f"Привет! Меня зовут {self.surname} {self.name}, мне {self.age} лет.")

    def add_grades(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)

students = [Person("Иван", "Иванов", 15), 
            Person("Петр", "Петров", 16), 
            Person("Анна", "Сидорова", 15)]
# тут записываются рандомные оценки от 1 до 5 после чего выводит средний балл каждого студента
for student in students:
    for i in range(5):
        student.add_grades(random.randint(1, 5))
    print(f"{student}: средний балл - {student.get_average_grade()}")

# сортировка листа студентов по убыванию среднего балла
students.sort(key=lambda x: x.get_average_grade(), reverse=True)
print("Список учеников в порядке убывания среднего балла:")
for student in students:
    print(f"{student}: средний балл - {student.get_average_grade()}")
# класс точки где просто инит имеется с x и y 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# класс прямоугольника 
class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right
    # Площадь
    def area(self):
        return abs((self.bottom_right.x - self.top_left.x) * (self.top_left.y - self.bottom_right.y))
    # Периметр 
    def perimeter(self):
        width = abs(self.bottom_right.x - self.top_left.x)
        height = abs(self.top_left.y - self.bottom_right.y)
        return 2 * (width + height)
    # Проверка находится ли точка внутри прямоугольника 
    def has_point(self, point):
        return (self.top_left.x <= point.x <= self.bottom_right.x and self.bottom_right.y <= point.y <= self.top_left.y)


point1 = Point(1, 5)
point2 = Point(7, 2)

rect1 = Rectangle(point1, point2)
# Площадь и периметр прямоугольника
print(f"Площадь прямоугольника : {rect1.area()}")
print(f"Периметр прямоугольника : {rect1.perimeter()}")

point3 = Point(11, 11)
point4 = Point(2, 3)

rect2 = Rectangle(point3, point4)
print(f"Площадь прямоугольника : {rect2.area()}")
print(f"Периметр прямоугольника : {rect2.perimeter()}")

# Проверка находится ли точка внутри прямоугольника
print(rect1.has_point(point3))
print(rect1.has_point(point4))