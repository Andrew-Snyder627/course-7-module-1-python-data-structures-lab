# This module contains functions to process student data.

def format_student_data(student):
    """
    Format student data for display.
    The function should return a formatted string containing:
    - Student ID
    - Student Name
    - Major
    """
    sid, name, major = student
    return f"ID: {sid} | Name: {name} | Major: {major}"


def display_students(student_list):
    """
    Display all students in a formatted way.
    Loop through the student_list and print each student using format_student_data().
    """
    for student in student_list:
        print(format_student_data(student))


def student_generator(student_list, major):
    """
    Generate student records lazily for a given major. Should be more memory efficient
    """
    return (student for student in student_list if student[2].lower() == major.lower())
