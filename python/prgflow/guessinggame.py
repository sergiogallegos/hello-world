answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please guess higher")
elif guess > answer:
    print("Please guess lower")
else:
    print("You got it first time")


# Variables Excersice

x = input("Put X value")
y = input("Put Y value")

if x > y:
    print("x is greater than y")
elif x == y:
    print("x equals y")
else:
    print("x is smaller than y")
