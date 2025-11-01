Learning_Disability = input("does the student have a learning disability? (yes/no): ")
attendence = input("does the student have good attendance? (yes/no): ")
grade = input("what is the student's grade percentage? (0-100): ")
if Learning_Disability == "yes" and attendence == "yes" and int(grade) >= 70:
    print("The student is eligible for the exam.")
elif Learning_Disability == "no" and attendence == "yes" and int(grade) >= 80:
    print("The student is eligible for the exam.")
else:
    print("The student is not eligible for the exam.")