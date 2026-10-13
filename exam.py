medical_cause = input("Does the student have a medical cause (y/n)? ").strip().lower()

if medical_cause == "y":
    print("The student is allowed to take the exam.")
else:
    attendance = int(input("Enter the attendance of the student. "))
    if attendance >= 75:
        print("The student is allowed to take the exam")
    else:
        print("The student is not allowed to take the exam.")