# This code calculates the mean of a student's 3 exam scores and outputs the student's mean exam score

# Define the exam_mean function for calculating the mean of 3 exams
def exam_mean(a, b, c):
  '''Do the exam mean by adding the three scores up and dividing by 3, return a variable'''
  mean = (a+b+c)/3
  return mean

# Define the project_mean function for calculating the mean of 2 projects
def project_mean(a, b):
  '''Do the project mean by adding the two scores up and dividing by 2, return a variable.'''
  mean = (a+b)/2
  return mean

# Define the semester_grade function for calculating the Student's Final Grade
def semester_grade(a,b):
  '''Divide the exam and project grades by 100, and then multiply by 60 and 40, respectively.
  Then add the two scores up to get the final grade.
  Return a variable."
  
  exam_grade = (a/100) * 60
  project_grade = (b/100) * 40

  # Add the values up to get the final grade
  final_grade = exam_grade + project_grade
  return final_grade

# Take user input for each of the three exam scores
exam_score1 = float(input("Exam 1 Score: "))
exam_score2 = float(input("Exam 2 Score: "))
exam_score3 = float(input("Exam 3 Score: "))

# Take user input for each of the two project scores
project_score1 = float(input("Project 1 Score: "))
project_score2 = float(input("Project 2 Score: "))

# Calculate the exam average for the semester by calling the exam_mean function.
exam_average = exam_mean(exam_score1, exam_score2, exam_score3)

# Calculate the project average for the semester by calling the project_mean function.
project_average = project_mean(project_score1, project_score2)

# Calculate the semester grade for the student by calling the semester_grade function.
grade = semester_grade(exam_average, project_average)

# Print the inputs and output
print(f"\nThe Student's three exam scores: {exam_score1}, {exam_score2}, {exam_score3}")
print(f"The Student's mean exam score is: {exam_average:.2f}")
print(f"\nThe Student's two project scores: {project_score1}, {project_score2}")
print(f"The Student's mean project score is: {project_average:.2f}")
print(f"The Student's Final Grade is: {grade:.2f}")

# Display a final input to keep the program open until the user shuts it down
var = input("\nPress enter to close the program")
