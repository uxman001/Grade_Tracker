# Student Grade Tracker

subjects = {}
num_subjects = int(input("Enter the number of subjects: "))

# Input grades
for i in range(num_subjects):
    subject = input(f"\nEnter the name of subject {i + 1}: ")
    grade = float(input(f"Enter the grade for {subject}: "))
    subjects[subject] = grade

# Display grades
print("\n--- Student Grades ---")
for subject, grade in subjects.items():
    print(f"{subject}: {grade}")

# Calculate average
average = sum(subjects.values()) / len(subjects)

print(f"\nAverage Grade: {average:.2f}")