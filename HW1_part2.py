# This code calculates the mean of a student's 3 exam scores and outputs the student's mean exam score

# Define the exam_mean function for calculating the mean of 3 numbers
def exam_mean(a, b, c):
  mean = (a + b + c)/3
  return mean

# Define the inputs
exam1 = 92
exam2 = 64
exam3 = 88

# Call the function
student_avg = exam_mean(exam1, exam2, exam3)

print('Exam Average:' student_avg)
