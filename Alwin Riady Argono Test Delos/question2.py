def sourCandy(student, candy, start):
    temp = 0
    if candy > student:
        temp = candy-student + start -1
    if student > candy:
        temp = student - candy + start
    
    if temp > student:
        return temp - student
    return temp


print("Enter the Student, Candy and start of the student(seperated by whitespace): ")
candy = list(map(int, input().split()))

print("Student Number: ", sourCandy(candy[0], candy[1], candy[2]))

