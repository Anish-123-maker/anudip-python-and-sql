def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0
def print_student_averages(students):
    for student_id, info in students.items():
        name = info['name']
        grades = info['grades']
        average = calculate_average(grades)
        print(f"{name}'s average grade is: {average:.2f}")
students = {
    'student1': {'name': 'Alice','age': 20,'grades': [90, 85, 88]},
    'student2': {'name': 'Bob','age': 21,'grades': [78, 82, 85]},
    'student3': {'name': 'Charlie','age': 22,'grades': [92, 90, 94]}
}
print_student_averages(students)
