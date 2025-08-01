print("Student Grade")
Marks = int(input("Enter the Total Marks of a student :"))

if(Marks >= 95):
    print("The Student got O Grade")
elif(Marks >= 80 and Marks <= 90):
    print("The Student got A+ Grade")
elif(Marks >= 70 and Marks < 80):
    print("The Student got A Grade")
elif(Marks >= 60 and Marks < 70):
    print("The Student got B+ Grade")
elif(Marks >= 50 and Marks < 60):
    print("The Student got B Grade")
elif(Marks >= 40 and Marks < 50):
    print("The Student got C Grade")
else:
    print("The Student Faild in an Exam ")

