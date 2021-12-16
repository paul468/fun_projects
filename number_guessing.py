import random
if __name__ == "__main__":
    min = int(input("Enter the minimal amount for the guessing game!"))
    max = int(input("Enter the maximal amount for the guessing game!"))
    num = random.randrange(min, max)
    found=False
    while not found:
        guess = int(input("Enter your guess here: "))
        if guess > num:
            print("go lower!")
        elif guess < num:
            print("go higher!")
        elif guess == num:
            print("You got it! The answer was " + str(num))
            found = True