# https://app.codingrooms.com/w/wngLzayImCaC
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lowname1 = name1.lower()
lowname2 = name2.lower()

combname = lowname1 + lowname2

s1 = combname.count("t") + combname.count("r") + combname.count("u") + combname.count("e") 
s2 = combname.count("l") + combname.count("o") + combname.count("v") + combname.count("e") 

score = str(s1) + str(s2)

if int(score) >= 90 or int(score) <= 10:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) <= 50 and int(score) >=40:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")