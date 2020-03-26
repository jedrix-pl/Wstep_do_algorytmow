import numpy as np
import random
from matplotlib import pyplot as plt


def gen_grades(min=2.0, max=5.5):

    grades_matrix = np.empty((5, 5))

    for element in np.nditer(grades_matrix, op_flags=['readwrite']):
        element[...] = random.randint(min*2, max*2) / 2

    print("\nGRADES:\n", grades_matrix, '\n')

    return grades_matrix


def fail_count(grades, n=2):

    students_failed = 0
    for index, row in enumerate(grades):
        failed_subject = 0
        for grade in row:
            if grade < 3:
                failed_subject += 1

        if failed_subject >= n:
            students_failed += 1
            print(f"Student{index+1}(row {index}) failed at least {n} exam(s)")

    return students_failed


def count_average(grades):
    average = np.average(grades)

    return average


def best_stud(grades):
    greatest_grade = np.amax(grades)
    students = []
    for index, row in enumerate(grades):
        if greatest_grade in row:
            stud = [np.sum(row == greatest_grade), index]
            students.append(stud)

    for student in students:
        best_count = 0
        if student[0] >= best_count:
            best_count = student[0]

    for std in students:
        if std[0] == best_count:
            print(f"Student{std[1]+1} scored {greatest_grade} {std[0]} time(s)!")


def visual_grades(grades):
    bins = np.array([2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6])

    for ex_col_index, ex_column in enumerate(grades.transpose()):
        plt.hist(ex_column, bins=bins, align='left', color='limegreen', edgecolor='green')
        plt.title(f"Subject {ex_col_index + 1}")
        plt.xlabel("Grade")
        plt.ylabel("Frequency")
        plt.show()


def show_min_max_avg(grades):
    avg_list = []
    for stud in grades:
        stud_avg = count_average(stud)
        avg_list.append(stud_avg)

    min_avg = min(avg_list)
    max_avg = max(avg_list)

    print(f"\nMAX: {max_avg}, MIN: {min_avg}\n")


def show_students_above_4(grades):
    for index, stud in enumerate(grades):
        stud_avg = count_average(stud)
        if stud_avg >= 4:
            print(f"Student{index+1} got average not less than 4.0!")

if __name__ == '__main__':

    GRADES = gen_grades()
    print(f"GRADES^T:\n{GRADES.transpose()}\n")

    fail_count(GRADES)

    show_min_max_avg(GRADES)

    print(f"The best grade is {np.amax(GRADES)}\n")

    best_stud(GRADES)

    visual_grades(GRADES)

    print("\n")
    show_students_above_4(GRADES)
