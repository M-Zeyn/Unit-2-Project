#import random and time
import random
import time

#greet the user
name = input("Enter your name: ")
print("HELLO",name.upper(),"!")

#explain the rules of the quiz
# use time to give the user time to read
print("This quiz was made to raise awareness about SDG #4: Quality Education")
time.sleep(3)
print("There are 10 questions")
time.sleep(2)
print("If you get a question right you will gain 50 points ")
time.sleep(4)
print("If you get a question wrong you will lose 25 points")
time.sleep(4)
print("Try to get the highest score")
time.sleep(1)
print("Good luck")

#create list of questions
questions_list = ["What is the main goal of SDG 4 (Quality Education)?",
                  "How many children were out of school globally in 2020?",
                  "What does inclusive education mean?",
                  "What does SDG stand for?",
                  "What is a key challenge/problem when trying to achieve quality education?",
                  "Which region has the highest rate of children out of school?",
                  "What role does technology play in SDG 4 (Quality Education)? ",
                  "What percentage of schools lack basic infrastructure?",
                  "How does education impact poverty?",
                  "What is a benefit of early childhood education?",
                  "Who is responsible for achieving SDG 4 (Quality Education)?",
                  "What year is the target year for achieving SDG 4 (Quality Education)?",
                  "What is the connection between education and gender equality?",
                  "Which option is not a focus of SDG 4 (Quality Education)?"]

# create list for options

options_list = ["A", "B", "C", "D",
                "A", "B", "C", "D",
                "A", "B", "C", "D",
                "A", "B", "C", "D",
                "A", "B", "C", "D",
                "A", "B", "C", "D",
                "A", "B", "C", "D",
                "A", "B", "C", "D",
                "A", "B", "C", "D",
                "A", "B", "C", "D",
                "A", "B", "C", "D",
                "A", "B", "C", "D",
                "A", "B", "C", "D",
                "A", "B", "C", "D",
                "A", "B", "C", "D",]

#create list for answers
answers_list = ["B", "C", "A", "B", "A", "D", "B", "B", "A", "B", "D", "C", "B", "B", "B"]


