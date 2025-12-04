# Grade-Book-Analyzer.py

# Author : Manpreet Kaur

# Date : 3-December-2025

# project : Grade-Book-Analyzer --- Analyze and Report Student Grades using Python

import csv   # importing the csv module

# Creating the welcome_message function that will print the welcome message when you run this program

def welcome_message():   
    print("Welcome to Grade-Book-Analyzer !")
    print("Choose data input method : ")
    print("1. Manual input")
    print("2. Load from a CSV file")
    
# Creating the manual_input function which will take manual entries from the user
# and return a dictionery named students
    
def manual_input():
    students={}
    n=int(input("Enter the number of students : "))
    for i in range(n):
        name=input("Enter the name of the student : ")
        marks=int(input(f"Enter the marks of {name} : "))
        students[name]=marks
    return students

# Creating the load_CSV function which will import the data from a pre-existing csv file
# and return a dictionery named students

def load_CSV(filename):
    students={}
    with open(filename,newline="") as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            name=row[0]
            marks=int(row[1])
            students[name]=marks
    return students

# Creating the function calculate_avergae that will calculate the average marks of the students
# and return the average

def calculate_average(marks_dict):
    total=sum(marks_dict.values())
    count=len(marks_dict)
    average=total/count
    return round(average,2)

# Creating the function calculate_median that will calculate the median marks of the students
# and return the median

def calculate_median(marks_dict):
    marks_list=sorted(marks_dict.values())
    n=len(marks_list)
    if n%2==0:
        median=(marks_list[n//2-1]+marks_list[n//2])/2
    else:
        median=marks_list[n//2] 
    return round(median,2) if isinstance(median, float) else median 

# Creating the function find_max_score that will find the maximum score ,
# scored by the student and return the maximum score and the student name with max score

def find_max_score(marks_dict):
    max_score=max(marks_dict.values())
    max_students=[name for name, score in marks_dict.items() if score == max_score ]
    return max_score, max_students

# Creating the function find_min_score that will find the minimum score ,
# scored by the student and return the minimum score and the student name with min score

def find_min_score(marks_dict):
    min_score=min(marks_dict.values())
    min_students=[name for name, score in marks_dict.items() if score == min_score ]
    return min_score, min_students

# Grade Assignment

# Creating a function assign_grades that will assign the grades to the students according to their score
# and add the score to a dictionery

def assign_grades(marks_dict):
    grades={}
    for student, marks in marks_dict.items():
        if marks >= 90:
            grade="A"
        elif marks >= 80:
            grade="B"
        elif marks >= 70:
            grade="C"
        elif marks >= 60:
            grade="D"
        else:
            grade="F"
        grades[student]=grade
    return grades

# Creating a function grade_distribution that will count the number of students getting a 
# corresponding grade and return the grade destribution

def grade_distribution(grades_dict):
    distribution={"A":0,"B":0,"C":0,"D":0,"F":0}
    for grade in grades_dict.values():
        distribution[grade]+==
    return distribution

# Pass / Fail Filter using list comprehension

# Creating a function filter_pass_fail that will filter all the failed and passed students
# separately and return the number of failed and passed students along with their names 

def filter_pass_fail(marks_dict):
    passed=[name for name, marks in marks_dict.items() if marks >=40 ]
    failed=[name for name, marks in marks_dict.items() if marks < 40 ]
    return passed, failed

# Results Table Printing function : that will print the final results table

def print_results_table(marks_dict, grades_dict):
    print("Name             Marks    Grade")
    print("-------------------------------------")
    for name in marks_dict:
        print(f"{name:<15}    {marks_dict[name]:<7}    {grades_dict[name]}")
    print("-------------------------------------")

# this main function will print the welcome message and take the choice from the user that 
# user wants to import the csv file or write the data manually and many more things .

def main():
    welcome_message()
    choice=input("Enter your choice (1 or 2) : ")
    if choice=="1":
        students_marks=manual_input()
    elif choice=="2":
        filename=input("Enter CSV filename : ")
        students_marks=load_CSV(filename)
    else:
        print("Invalid Choice ! , Exit caused due to Invalid Choice .")
        
# Statistical summary : calling the functions and storing them in the variables

    avg=calculate_average(students_marks)
    med=calculate_median(students_marks)
    max_score,max_students=find_max_score(students_marks)
    min_score,min_students=find_min_score(students_marks)
    
# printing the final results

    print("Statistics Summary : ")
    print(f"Average marks : {avg}")
    print(f"Median marks : {med}")
    print(f"Max Score : {max_score} by {','.join(max_students)}")
    print(f"Mix Score : {min_score} by {','.join(min_students)}")
    
# Assigned grades : printing the grade distribution

    grades=assign_grades(students_marks)
    dist=grade_distribution(grades)
    print("Grade Distribution : ")
    for grade, count in dist.items():
        print(f"{grade} : {count} students")
    
# Pass / Fail filtering : printing the filtered pass and failed students 

    passed_students, failed_students = filter_pass_fail(students_marks)
    print(f"Passed Students ({len(passed_students)}) : {','.join(passed_students)}")
    print(f"Failed students ({len(failed_students)}) : {','.join(failed_students)}")
    
# Printing the final table

    print_results_table(students_marks,grades)

# User Loop to repeat or exit : that will ask user that if he want to analyse another grade book or
# want to exit the Grade-Book-Analuzer

    while True:
        repeat=input("Do you want to analyze another set? (yes/no) : ").strip().lower()
        if repeat=="yes":
            main()
            break
        elif repeat=="no":
            print("Thank you for using Grade-Book-Analyzer ! ")
            break
        else:
            print("Invalid input, please enter yes or no.")
            
# these lines starts the main grade analyzer program by calling the main() funtion
            
if __name__=="__main__":
    main()