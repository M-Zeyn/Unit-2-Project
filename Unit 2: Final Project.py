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
print("You will be given 10 random multiple-choice questions")
time.sleep(3)
print("If you get a question right you will gain 50 points ")
time.sleep(3)
print("If you get a question wrong you will lose 25 points")
time.sleep(3)
print("Try to get the highest score")
time.sleep(1)
print("Good luck")
time.sleep(3)

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

options_list = [
    ["A. End poverty", "B. Provide quality education for all", "C. Achieve gender equality", "D. Promote economic growth"],
    ["A. 58 million", "B. 75 million", "C. 244 million", "D. 300 million"],
    ["A. Ensure free primary and secondary education", "B. Provide free healthcare for all", "C. End hunger", "D. Protect marine life"],
    ["A. Education only for boys", "B. Education for people of all genders and abilities", "C. Education for rich families only", "D. Education that excludes minority groups"],
    ["A. Sustainable Development Goals", "B. Social Development Goals", "C. Special Development Goals", "D. School Development Goals"],
    ["A. Lack of teachers", "B. Limited access to resources", "C. Financial barriers", "D. All of the above"],
    ["A. Europe", "B. Sub-Saharan Africa", "C. North America", "D. East Asia"],
    ["A. No role", "B. Improves access and quality", "C. Replaces teachers", "D. Only for wealthy countries"],
    ["A. 20%", "B. 50%", "C. 30%", "D. 10%"],
    ["A. No impact", "B. Reduces poverty by providing skills", "C. Increases poverty", "D. Has only minor effects"],
    ["A. Better long-term health", "B. Improved job prospects", "C. Social development", "D. All of the above"],
    ["A. Only governments", "B. Only NGOs", "C. Everyone", "D. Only educators"],
    ["A. 2025", "B. 2030", "C. 2040", "D. 2050"],
    ["A. Education empowers women and girls", "B. Education has no role in gender equality", "C. Education closes opportunity gaps", "D. Education reduces discrimination"],
    ["A. Adult literacy", "B. Access to clean water", "C. Technical skills training", "D. Vocational training"]
]

#create list for answer
answers_list = ["B", "C", "A", "B", "A", "D", "B", "B", "A", "B", "D", "C", "B", "B", "B"]

#make score 0
#make variable for loop

score = 0
used_questions = []

#create loop
for i in range(10):
    index = random.randint(0, len(questions_list)-1)
    while index in used_questions:
        index = random.random.randint(0, len(questions_list)-1)
        used_questions.append(index)

#display question to user
print("Question", i + 1, ":", questions_list[index])
for option in options_list:
    print(option)

#get the input from the user
user_input = input("Your Answer: ")

# check answer
# if right give 50
# if wrong take 25

if user_input == answers_list[index]:
    print("Correct! You Get 50 Points!")
    score+=50
elif user_input in ["A","B","C","D"]:
    print("Incorrect! The correct Answer Was",answers_list[index] + ".""You Lose 25 Points!")
    score-=25
else:
    print("Invalid input, No Points Were Awarded or Deducted")







