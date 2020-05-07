#This is a python quiz program that has five questions and each question has four option using dictionaries
q1 = """Is python case sensitive when dealing with indentifiers?
a. Yes
b. No
c. Machine Dependent
d. None"""
q2 = """Which of the following is not a keyword?
a. eval
b. assert
c. local
d. pass"""
q3 = """Which of these is floor division?
a. /
b. //
c. %
d. None"""
q4 = """What is the output of this 3*1**3?
a. 27
b. 9
c. 3
d. 1"""
q5 = """"a"+"bc"=?
a. a
b. bc
c. bca
d. abc"""

#Here questions and the answer to that question is stored as a key value pair
questions = {q1:"a",q2:"a",q3:"b",q4:"c",q5:"d"}

name =input("enter your name:")

print("hello",name,"welcome to the quiz world")

#To print que and option we need to iterate through the dictionary
score=0
for i in questions:
    print()
    #print the questions
    print(i)
    #Here we have given option to user to skip the question
    flag1=input("Do you want to skip this question (yes/no):")
    if flag1=="yes":
        continue

#we need user to enter answers here and that is stored in ans variable
    ans = input ("enter the answer (a/b/c/d):")
    if ans==questions[i]:
        print("correct answer,you got 1 point")
        score =score+1
    else:
        print("wrong answer,you lost 1 point")
        score =score-1
    #Here We have given the option to user to quit the quiz
    flag2 = input("Do you want to quit (yes/no)")
    if flag2 =="yes":
        break
print("Final score is:",score)
    
