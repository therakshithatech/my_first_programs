name=input("enter your name:")
age=int(input("enter your age:"))
college=input("enter your college name:")
cource=("enter the cource:")

python_marks=int(input("enter python marks:"))
maths_marks=int(input("enter maths marks:"))
science_marks=int(input("enter science marks:"))
total=python_marks+maths_marks+science_marks
average=total/3
percentage=(total/300)*100

elegible_to_vote=age>=18
passed_all=python_marks>=35 and maths_marks>=35 and science_marks>=35
python_greater=python_marks>maths_marks
average_sixty=average>=60

subjects=["python","maths","science"]
python_in_list="python"in subjects
english_not_in_list="english" not in subjects

num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
bit_and=num1&num2
bit_or=num1|num2
bit_xor=num1^num2
left_shift=num1<<1
right_shift=num1>>1
         
print("\n======student information system======")
print("name:",name)
print("age:",age)
print("college:",college)
print("cource:",cource)

print("total:",total)
print("average:",average)
print("percentage:",percentage)

print("elegible to vote:",elegible_to_vote)
print("passed all:",passed_all)
print("python.maths:",python_greater)
print("average>=60:",average_sixty)

print("python in subjects:",python_in_list)
print("english not in subjects;",english_not_in_list)

print("bitwise AND:",bit_and)
print("bitwise OR:",bit_or)
print("bitwise xor:",bit_xor)
print("left shift:",left_shift)
print("right shift:",right_shift)         
         
         
         
