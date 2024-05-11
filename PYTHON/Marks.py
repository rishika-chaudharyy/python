marks = float(input("Enter the percentage of students: "))

if marks >= 80 and marks <= 100:
    print("Very good")
elif marks >= 61 and marks < 80:
    print("Good")
elif marks >= 41 and marks <= 60:
    print("Average")
elif marks <= 40:
    print("Poor/Fail")
else:
    print("Enter valid marks")
