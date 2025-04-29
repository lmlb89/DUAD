

def menu():
    print("Select an option:")
    print("1. Enter student information")
    print("2. Check student info")
    print("3. Check top 3 students")
    print("4. Check total average")
    print("5. Export all info to CSV file")
    print("6. Import data from existing CSV file ")
    print("7. Exit")

    while True:
        try:
            choice = int(input("Enter your choice (1-7): "))
            if 1 <= choice <= 7:
                return choice
            else:
                print("Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
            
menu()