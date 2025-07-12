import random

name = "Reggie"
question = "Am I gonna be a successful software engineer one day?"
answer = random.randint(1, 9)
magic_answer = "Magic 8-Ball's answer:"

if answer == 1:
    response = "Yes - definitely"
elif answer == 2:
    response = "It is decidedly so"
elif answer == 3:
    response = "Without a doubt"
elif answer == 4:
    response = "Reply hazy, try again"
elif answer == 5:
    response = "Ask again later"
elif answer == 6:
    response = "Better not tell you now"
elif answer == 7:
    response = "My sources say no"
elif answer == 8:
    response = "Outlook not so good"
elif answer == 9:
    response = "Very doubtful"

print(name,"asks:",question)
print(magic_answer,response)