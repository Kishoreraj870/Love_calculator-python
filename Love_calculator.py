
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



name1_lower=name1.lower()
name2_lower = name2.lower()
whole_name = name1_lower+name2_lower

score_T = whole_name.count("t")
score_R = whole_name.count("r")
score_U = whole_name.count("u")
score_E = whole_name.count("e")
total_score_1 = score_T+score_R+score_U+score_E

score_L = whole_name.count("l")
score_O = whole_name.count("o")
score_V = whole_name.count("v")
score_E = whole_name.count("e")
total_score_2 = score_L+score_O+score_V+score_E

total_score = int(str(total_score_1) + str(total_score_2))

if(total_score<10 or total_score>90):
  print(f"Your score is {total_score}, you go together like coke and mentos.")
elif(total_score>40 and total_score<50):
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")

