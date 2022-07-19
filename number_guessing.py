import random




num = input("enter the range you wanna play with: ")
if num.isdigit():
    num = int(num)
    if num <= 0:
        print("Please type a number greater than Zero next time: ")
        quit()
else:
    print("OOPS! Invalid input. Please type a number next time. ")


generated_number = random.randrange(0, num)

no_of_guess = 0
while True:
    no_of_guess += 1
    user_guess = input(" Try guessing the number computer has guessed: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else :
        print("Please type a number next time. ")
        continue

    print("your guess is: ", user_guess)
    print("Computer's guess is: ", generated_number)
    if user_guess == generated_number:
        print("You won.")
        break
    elif user_guess > generated_number:
        print("You guessed higher this time.")
    else:
        print("You guessed lower this time.")
    
print(' You guessed the number in ', no_of_guess)