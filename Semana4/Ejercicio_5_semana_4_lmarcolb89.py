

#5. Dada `n` cantidad de notas de un estudiante, calcular:
    #1. Cuantas notas tiene aprobadas (mayor a 70).
    #2. Cuantas notas tiene desaprobadas (menor a 70).
    #3. El promedio de todas.
    #4. El promedio de las aprobadas.
    #5. El promedio de las desaprobadas.

n = int(input("Enter the number of grades: "))
grades = []

for i in range(n):
    grade = int(input(f"Enter your grade {i+1}: "))
    grades.append(grade)

passed = [n for n in grades if n > 70]
failed = [n for n in grades if n < 70]

print(f"Passed: {len(passed)}")
print(f"Failed: {len(failed)}")
print(f"Total average: {sum(grades)/len(grades):.2f}")
print(f"Passed average: {sum(passed)/len(passed) if passed else 0:.2f}")
print(f"Failed average: {sum(failed)/len(failed) if failed else 0:.2f}")

