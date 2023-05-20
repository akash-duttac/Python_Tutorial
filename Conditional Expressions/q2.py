# 2. Write a program to find out whether a student is pass or fail if it requires
# a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

sub1 = int(input("Enter subject 1 marks: "))
sub2 = int(input("Enter subject 2 marks: "))
sub3 = int(input("Enter subject 3 marks: "))

# if sub1 + sub2 + sub3 >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
#     print("PASS")
# else: print("FAIL")

if sub1 <= 33 or sub2 <= 33 or sub3 <= 33:
    print("FAIL: All subject scores must be above 33%")
elif (sub1+sub2+sub3)/3 <= 40:
    print("FAIL: TOTAL score must be greater than 40%")
else:
    print("PASS")