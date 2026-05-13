# 3. Duplique el proyecto [Sistema de Control de Estudiantes](https://www.notion.so/Sistema-de-Control-de-Estudiantes-be23e9a75d484d35a9fdb527f741854c?pvs=21) y modifíquelo para usar objetos para guardar la información de los estudiantes (creando una clase de `Student`).
#    1. Hay que cambiar los estudiantes de diccionarios a objetos.
#    2. Hay que convertir la data del csv (que viene por defecto en formato de diccionario) a objetos al importarla.
#    3. Hay que convertir los objetos a diccionarios para poder exportarlos a csv.
#    4. Hay que modificar el acceso a los keys para accesar a atributos.
#        1. student[’Name’] → student.name

import csv

class Student:
    def __init__(self, name, section, spanish, english, science):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.science = science
    
    def create_from_dict(data):
        return Student(
            data['Name'],
            int(data['Section']),
            int(data['Spanish']),
            int(data['English']),
            int(data['Science'])
        )
    
    def to_dict(self):
        return {
            'Name': self.name,
            'Section': self.section,
            'Spanish': self.spanish,
            'English': self.english,
            'Science': self.science
        }
    
    def __str__(self):
        return (f"Student(Name: {self.name}, Section: {self.section}, "
                f"Grades: Spanish={self.spanish}, English={self.english}, Science={self.science})")

class GradeManager:
    def __init__(self):
        self.students = []
        self.filename = "students.csv"
    
    def validate_grade(self, value):
        return 1 <= value <= 100
    
    def input_int(self, prompt, validator=None):
        while True:
            try:
                value = int(input(prompt))
                if validator is None or validator(value):
                    return value
                print("Invalid input. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
    
    def input_student_data(self):
        print("\nEnter student details:")
        name = input("Name: ").strip()
        while not name:
            print("Name cannot be empty!")
            name = input("Name: ").strip()
        
        section = self.input_int("Section number: ")
        
        print("Enter grades (1-100):")
        spanish = self.input_int("Spanish: ", self.validate_grade)
        english = self.input_int("English: ", self.validate_grade)
        science = self.input_int("Science: ", self.validate_grade)
        
        return Student(name, section, spanish, english, science)
    
    def add_student(self, student):
        self.students.append(student)
    
    def save_to_csv(self):
        with open(self.filename, 'w', newline='') as csvfile:
            fieldnames = ['Name', 'Section', 'Spanish', 'English', 'Science']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for student in self.students:
                writer.writerow(student.to_dict())
    
    def load_from_csv(self):
        self.students = []
        try:
            with open(self.filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.students.append(Student.create_from_dict(row))
        except FileNotFoundError:
            print(f"File {self.filename} not found. Starting with empty list.")
    
    def display_all_students(self):
        if not self.students:
            print("\nNo students in records.")
        else:
            print("\nAll Students:")
            for idx, student in enumerate(self.students, 1):
                print(f"{idx}. {student}")

def main():
    print("Student Grade Management System")
    
    manager = GradeManager()
    manager.load_from_csv()
    
    while True:
        print("Menu:")
        print("1. Add new student")
        print("2. View all students")
        print("3. Save and exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            student = manager.input_student_data()
            manager.add_student(student)
            print(f"Added student: {student}")
        
        elif choice == '2':
            manager.display_all_students()
        
        elif choice == '3':
            manager.save_to_csv()
            print(f"\Data saved to {manager.filename}. Exiting program.")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()


