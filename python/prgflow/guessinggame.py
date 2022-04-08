answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("sorry, you have not guessed correectly")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("sorry, you have not guessed correectly")
else:
    print("You got it first time")


# Variables Excersice

x = input("Put X value: ")
y = input("Put Y value: ")

if x > y:
    print("x is greater than y")
elif x == y:
    print("x equals y")
else:
    print("x is smaller than y")
