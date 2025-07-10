
def add_students(students):
    while True:
        student = {}
        print("\nEnter student information (or type 'done' to finish):")
        
        student['name'] = input("Name: ")
        if student['name'].lower() == 'done':
            break
            
        student['group'] = input("Group number: ")
        
        student['english'] = get_valid_grade("English grade (1-100): ")
        student['spanish'] = get_valid_grade("Spanish grade (1-100): ")
        student['science'] = get_valid_grade("Science grade (1-100): ")
        student['social_studies'] = get_valid_grade("Social studies grade (1-100): ")
        
        student['average'] = calculate_average(student)
        students.append(student)
        print(f"Student {student['name']} added successfully!")

def get_valid_grade(prompt):
    while True:
        try:
            grade = int(input(prompt))
            if 1 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 1 and 100.")
        except ValueError:
            print("Please enter a valid number.")

def calculate_average(student):
    return (student['english'] + student['spanish'] + student['science'] + student['social_studies']) / 4

def show_all_students(students):
    if not students:
        print("No student data available.")
        return
    
    print("\nAll Students:")
    print("-" * 60)
    print(f"{'Name':<20}{'Group':<10}{'English':<10}{'Spanish':<10}{'Science':<10}{'Average':<10}")
    print("-" * 60)
    
    for student in students:
        print(f"{student['name']:<20}{student['group']:<10}{student['english']:<10}"
              f"{student['spanish']:<10}{student['science']:<10}{student['average']:<10.2f}")

def show_top_3(students):
    if not students:
        print("No student data available.")
        return
    
    sorted_students = sorted(students, key=lambda x: x['average'], reverse=True)
    top_3 = sorted_students[:3]
    
    print("\nTop 3 Students:")
    print("-" * 60)
    print(f"{'Name':<20}{'Group':<10}{'Average':<10}")
    print("-" * 60)
    
    for student in top_3:
        print(f"{student['name']:<20}{student['group']:<10}{student['average']:<10.2f}")

def show_total_average(students):
    if not students:
        print("No student data available.")
        return
    
    total = sum(student['average'] for student in students)
    average = total / len(students)
    print(f"\nTotal average for all students: {average:.2f}")
