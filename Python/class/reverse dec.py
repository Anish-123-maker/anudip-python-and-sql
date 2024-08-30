def reverse_dict(original_dict):
    reversed_dict = {}
    for student, grade in original_dict.items():
        if grade in reversed_dict:
            reversed_dict[grade].append(student)
        else:
            reversed_dict[grade] = [student]
    return reversed_dict
student_grades = {'Alice': 90, 'Bob': 85, 'Charlie': 90, 'David': 85}
reversed_grades = reverse_dict(student_grades)
print(reversed_grades)
