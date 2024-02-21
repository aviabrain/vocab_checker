import random

TOTAL_SCORE = 0

def check(level):

    score = 0
        
    for i in range(10):
        with open(f'vocab_{level}.txt', 'r') as file:
            lines = file.readlines()
            words = [word for line in lines for word in line.split()]
            random_word = random.choice(words)

        answer = input(f"Do you know this word '{random_word}' ? y/n ")
        if answer == 'y':
            score+=1
            
        else:
            score=score
            
    return score

a1score = check('a1')
a2score = check('a2')*1.2
b1score = check('b1')*1.6
b2score = check('b2')*1.8
c1score = check('c1')*2
c2score = check('c2')*2.4
print("\nThe test has complated!\n")
scores = [a1score,a2score,b1score,b2score,c1score,c2score]
TOTAL_SCORE = sum(scores)
print(TOTAL_SCORE,"/",100)

if TOTAL_SCORE <= 10:
    print("Your level is A1")
elif TOTAL_SCORE <= 22 and TOTAL_SCORE > 10:
    print("Your level is A2")
elif TOTAL_SCORE <= 38 and TOTAL_SCORE > 22:
    print('Your level is B1')
elif TOTAL_SCORE <= 56 and TOTAL_SCORE > 38:
    print('Your level is B2')
elif TOTAL_SCORE <= 76 and TOTAL_SCORE > 56:
    print("Your level is C1")
elif TOTAL_SCORE <= 100 and TOTAL_SCORE > 76:
    print("Your level is C2")