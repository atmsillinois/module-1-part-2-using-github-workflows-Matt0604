# This code calculates the mean of a student's 3 exam scores and outputs the student's mean exam score

# Define the exam_mean function for calculating the mean of 3 numbers
def exam_mean(a, b, c):
  mean = (a + b + c)/3
  return mean

# Take user input for each of the three exam scores
score1 = float(input("Exam 1 Score: "))
score2 = float(input("Exam 2 Score: "))
score3 = float(input("Exam 3 Score: "))

# Calculate the exam average for the semester
semester_average = exam_mean(score1, score2, score3)

# Print the inputs and output
print(f"\nThe Student's three exam scores: {score1}, {score2}, {score3}")
print(f"The Student's mean exam score is: {semester_average:.2f}")

var = input("Press enter to close the program")
