import random

secret = random.randint(1,10)
guess = int(input('숫자를 입력해보세요: '))

if guess > secret:
    print("too high")

if guess < secret:
    print("too low")

if guess == secret:
    print("just right")