import random
def guess_game(variable):
   for i in range(1,21):
        k = int(input())
        if k==variable:
            print(f"Good job, {kk}! You guessed my number in {i} guesses!")
            break;
        if k!=variable:
            print("Your guess is too low.")
            print("Take a guess")


print("Hello! What is your name?")
kk = input()
print(f"Well, {kk}, I am thinking of a number between 1 and 20.")
print("Take a guess")
random_number = random.randint(1, 20)
Res=guess_game(random_number)

