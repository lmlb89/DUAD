

import csv
import os

def export_to_csv(students):
    if not students:
        print("No student data to export.")
        return
    
    filename = "students_data.csv"
    try:
        with open(filename, 'w', newline='') as file:
            fieldnames = ['name', 'group', 'english', 'spanish', 'science', 'social_studies', 'average']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(students)
            
        print(f"Data successfully exported to {filename}")
    except Exception as e:
        print(f"Error exporting data: {e}")

def import_from_csv():
    filename = "students_data.csv"
    
    if not os.path.exists(filename):
        print(f"No CSV file found ({filename}). Please export data first.")
        return []
    
    students = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['english'] = int(row['english'])
                row['spanish'] = int(row['spanish'])
                row['science'] = int(row['science'])
                row['social_studies'] = int(row['social_studies'])
                row['average'] = float(row['average'])
                students.append(row)
                
        print(f"Data successfully imported from {filename}")
        return students
    except Exception as e:
        print(f"Error importing data: {e}")
        return []