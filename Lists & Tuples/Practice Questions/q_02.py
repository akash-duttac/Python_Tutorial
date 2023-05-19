# Write a program to accept the marks of 6 students and display them in a sorted manner.
marks1 = int(input("Enter marks of student 1 : "))
marks2 = int(input("Enter marks of student 2 : "))
marks3 = int(input("Enter marks of student 3 : "))
marks4 = int(input("Enter marks of student 4 : "))
marks5 = int(input("Enter marks of student 5 : "))
marks6 = int(input("Enter marks of student 6 : "))
marks_list = [marks1, marks2, marks3, marks4, marks5, marks6]
print("Unsorted list: "+str(marks_list))
marks_list.sort()
print("The sorted list: "+str(marks_list))