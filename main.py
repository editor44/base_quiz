#2706/2022 l Base Quiz

#import the random libary
import random

#globals and question lists 
score = 0
english = ["Computer", "Lake", "Food","Car","Man"]
right_answer = ["Rorohiko", "Roto", "Kai","Motokar","Tane"]
option_1 = ["Wrong Answer" , "Wrong Answer", "Wrong Answer","Wrong Answer","Wrong Answer"]
option_2 = ["Wrong Answer" , "Wrong Answer", "Wrong Answer","Wrong Answer","Wrong Answer"]

#define a function to generate a question
def generate_question(english,right_answer,option_1,option_2):
  global score
  print("What is the correct word for", english, "in maori")
  #Generate a random number to determine the sequence of questions
  random_sequence = random.randint(0,2)
  #seperate print statements for readability
  if(random_sequence == 0):
    print("A", option_1)
    print("B", option_2)
    print("C", right_answer)
    answer = input().lower()
    if answer == "c":
      score += 1
    else:
      print("incorrect.")
  if(random_sequence == 1):
    print("A", right_answer)
    print("B", option_1)
    print("C", option_2)
    answer = input().lower()
    if answer == "a":
      score += 1
    else:
      print("incorrect.")
  if(random_sequence == 2):
    print("A", option_1)
    print("B", right_answer)
    print("C", option_2)
    answer = input().lower()
    if answer == "b":
      score += 1
    else:
      print("incorrect.")
  
#generate 5 questions pulling possible answers from lists.
for i in range (0,5):
  generate_question(english[i],right_answer[i],option_1[i],option_2[i])

#print the score at the end of the quiz
print("Your final score was", score)

if score >= 4:
  print("You have passed")
else:
  print("You have failed")