# 6. Write a program to calculate the grade of a student from his marks from the following scheme:
#                                 90-100	Ex
#                                 80-90	    A
#                                 70-80	    B
#                                 60-70	    C
#                                 50-60	    D
#                                 <50	    F
marks = int(input("Enter marks: "))
flag = int(marks / 10)
if flag == 9:
    print("Excellent")
elif flag == 8:
    print("A")
elif flag == 7:
    print("B")
elif flag == 6:
    print("C")
elif flag == 5:
    print("D")
elif flag < 5:
    print("F")
