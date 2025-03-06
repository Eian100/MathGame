import random
import time

OPERATORS = ['+', '-', '*']
MIN_NUMBER = 1
MAX_NUMBER = 12
NUM_QUESTIONS = 10

def generate_question():
    left = random.randint(MIN_NUMBER, MAX_NUMBER)
    right = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(OPERATORS)

    expr = str(left) + ' ' + operator + ' ' + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
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
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print('---------------------------------')
print('You got', NUM_QUESTIONS - wrong, 'out of', NUM_QUESTIONS, 'questions right', 'in', total_time, 'seconds')

