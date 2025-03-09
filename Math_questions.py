import random
import time

OPERATORS = ['+', '-', '*']
MIN_NUMBER = 1
MAX_NUMBER = 12
NUM_QUESTIONS = 10
LEADERBOARD_file = 'leaderboard.txt'

def generate_question():
    left = random.randint(MIN_NUMBER, MAX_NUMBER)
    right = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(OPERATORS)

    expr = str(left) + ' ' + operator + ' ' + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
name = input('Enter your name: ')
print('---------------------------------')
input('Press Enter to start the quiz')
print('---------------------------------')

start_time = time.time()

for i in range(NUM_QUESTIONS):
    expr, answer = generate_question()
    while True:
        guess = input('Question #' + str(i + 1) + ': ' + expr + ' = ')
        if guess ==  str(answer):
         print('Correct!')
         break
        else:
            print('Incorrect!')
            wrong += 1
            break
            

end_time = time.time()
total_time = round(end_time - start_time, 2)

print('---------------------------------')
print('You got', NUM_QUESTIONS - wrong, 'out of', NUM_QUESTIONS, 'questions right', 'in', total_time, 'seconds')
LEADERBOARD_file = open('leaderboard.txt', 'a')
if(NUM_QUESTIONS - wrong == 10):
    LEADERBOARD_file.write(name + ' ' + str(NUM_QUESTIONS - wrong) + ' ' + str(total_time) + '\n')
print('---------------------------------')
print('10/10 - Times(no order):')
LEADERBOARD_file.close()
LEADERBOARD_file = open('leaderboard.txt', 'r')
leaderboard = LEADERBOARD_file.readlines()
leaderboard = [line.split() for line in leaderboard]
leaderboard.sort(key=lambda x: x[1], reverse=True)
for i, line in enumerate(leaderboard):
    print(i + 1, '.', line[0], line[1], line[2])
LEADERBOARD_file.close()
print('---------------------------------')

