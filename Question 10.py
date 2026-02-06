# HackerRank Python Question.

# Question 10:
# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

def student_average(student_marks,query_name):
    for key,value in student_marks.items():
        if key == query_name:
            average_score = sum(value) / len(value)
    print("{:.2f}".format(average_score))


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    student_average(student_marks,query_name)